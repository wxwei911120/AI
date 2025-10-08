#!/bin/bash

# AI營銷內容生成系統 - 快速部署腳本
# 此腳本將自動完成系統的初始化和部署

set -e  # 遇到錯誤立即退出

echo "🚀 AI營銷內容生成系統 - 自動部署開始"
echo "=================================================="

# 檢查系統要求
check_requirements() {
    echo "📋 檢查系統要求..."
    
    # 檢查Python
    if ! command -v python3 &> /dev/null; then
        echo "❌ 錯誤: 未找到Python 3"
        echo "請安裝Python 3.9-3.11版本"
        exit 1
    fi
    
    python_version=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
    echo "✅ Python版本: $python_version"
    
    # 檢查Docker
    if ! command -v docker &> /dev/null; then
        echo "❌ 錯誤: 未找到Docker"
        echo "請安裝Docker Desktop或Docker Engine"
        exit 1
    fi
    
    echo "✅ Docker版本: $(docker --version)"
    
    # 檢查Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        echo "❌ 錯誤: 未找到Docker Compose"
        echo "請安裝Docker Compose 2.0+"
        exit 1
    fi
    
    echo "✅ Docker Compose版本: $(docker-compose --version)"
    
    # 檢查NVIDIA GPU (可選)
    if command -v nvidia-smi &> /dev/null; then
        echo "✅ 檢測到NVIDIA GPU:"
        nvidia-smi --query-gpu=name,memory.total --format=csv,noheader,nounits | head -1
    else
        echo "⚠️  未檢測到NVIDIA GPU，將使用CPU模式"
        echo "   建議使用RTX 3090或更高級別的GPU以獲得最佳性能"
    fi
}

# 創建必要目錄
setup_directories() {
    echo "📁 創建項目目錄..."
    
    directories=(
        "checkpoints"
        "uploads"
        "outputs/images"
        "outputs/videos" 
        "outputs/text"
        "logs"
        "data"
    )
    
    for dir in "${directories[@]}"; do
        mkdir -p "$dir"
        echo "   ✅ $dir"
    done
}

# 設置環境配置
setup_environment() {
    echo "⚙️  設置環境配置..."
    
    if [ ! -f .env ]; then
        cp .env.example .env
        echo "✅ 已創建 .env 配置文件"
        echo "📝 請編輯 .env 文件設置必要的配置項："
        echo "   - POSTGRES_PASSWORD (數據庫密碼)"
        echo "   - JWT_SECRET_KEY (JWT密鑰)"
        echo "   - HUGGINGFACE_TOKEN (可選，用於下載模型)"
        echo ""
        read -p "是否現在編輯配置文件？(y/N): " edit_config
        if [[ $edit_config == "y" || $edit_config == "Y" ]]; then
            ${EDITOR:-nano} .env
        fi
    else
        echo "✅ 環境配置文件已存在"
    fi
}

# 創建Python虛擬環境
setup_python_env() {
    echo "🐍 設置Python虛擬環境..."
    
    if [ ! -d "ai_marketing_env" ]; then
        python3 -m venv ai_marketing_env
        echo "✅ 虛擬環境已創建"
    fi
    
    source ai_marketing_env/bin/activate
    echo "✅ 虛擬環境已激活"
    
    # 升級pip
    pip install --upgrade pip
    
    # 安裝PyTorch (CUDA版本)
    echo "📦 安裝PyTorch..."
    if command -v nvidia-smi &> /dev/null; then
        pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 torchaudio==2.1.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html
        echo "✅ 已安裝CUDA版PyTorch"
    else
        pip install torch torchvision torchaudio
        echo "✅ 已安裝CPU版PyTorch"
    fi
    
    # 安裝其他依賴
    echo "📦 安裝項目依賴..."
    pip install -r requirements/pt2.txt
    
    # 安裝額外依賴
    pip install fastapi uvicorn sqlalchemy psycopg2-binary redis celery gradio
    pip install transformers diffusers accelerate xformers
    pip install matplotlib plotly pandas requests pillow
    
    echo "✅ 所有依賴已安裝完成"
}

# 下載AI模型
download_models() {
    echo "🤖 下載AI模型..."
    echo "⚠️  注意: 模型總大小約50GB，請確保有足夠的網絡和存儲空間"
    
    read -p "是否開始下載模型？(Y/n): " download_confirm
    if [[ $download_confirm == "n" || $download_confirm == "N" ]]; then
        echo "⏭️  跳過模型下載，稍後可手動運行: python download_models.py"
        return 0
    fi
    
    python download_models.py
    echo "✅ 模型下載完成"
}

# 構建Docker鏡像
build_docker() {
    echo "🐳 構建Docker鏡像..."
    
    docker-compose build --parallel
    echo "✅ Docker鏡像構建完成"
}

# 啟動服務
start_services() {
    echo "🚀 啟動服務..."
    
    # 啟動基礎服務
    echo "   啟動數據庫和緩存服務..."
    docker-compose up -d postgres redis
    
    # 等待數據庫就緒
    echo "   等待數據庫啟動..."
    sleep 10
    
    # 初始化數據庫
    echo "   初始化數據庫..."
    docker-compose exec postgres psql -U ai_user -d ai_marketing -c "SELECT 1;" || {
        echo "   創建數據庫..."
        docker-compose exec postgres createdb -U ai_user ai_marketing
    }
    
    # 啟動AI服務
    echo "   啟動AI生成服務..."
    docker-compose up -d ai-generator celery-worker
    
    # 啟動Web界面
    echo "   啟動Web界面..."
    docker-compose up -d gradio-interface
    
    # 啟動監控服務
    echo "   啟動監控服務..."
    docker-compose up -d nginx prometheus grafana
    
    echo "✅ 所有服務已啟動"
}

# 健康檢查
health_check() {
    echo "🔍 執行健康檢查..."
    
    # 等待服務啟動
    sleep 30
    
    # 檢查API服務
    if curl -f http://localhost:8000/health &> /dev/null; then
        echo "✅ API服務運行正常"
    else
        echo "❌ API服務異常"
        return 1
    fi
    
    # 檢查Web界面
    if curl -f http://localhost:7860 &> /dev/null; then
        echo "✅ Web界面運行正常"
    else
        echo "❌ Web界面異常"
        return 1
    fi
    
    # 檢查數據庫
    if docker-compose exec postgres pg_isready -U ai_user &> /dev/null; then
        echo "✅ 數據庫連接正常"
    else
        echo "❌ 數據庫連接異常"
        return 1
    fi
    
    echo "✅ 所有服務健康檢查通過"
}

# 顯示部署信息
show_deployment_info() {
    echo ""
    echo "🎉 部署完成！系統已啟動並運行"
    echo "=================================================="
    echo ""
    echo "🌐 訪問地址:"
    echo "   Web界面:    http://localhost:7860"
    echo "   API服務:    http://localhost:8000"
    echo "   API文檔:    http://localhost:8000/docs"
    echo "   監控面板:   http://localhost:3000 (admin/admin)"
    echo ""
    echo "📊 服務狀態:"
    docker-compose ps
    echo ""
    echo "🛠️  常用命令:"
    echo "   查看日志:   docker-compose logs -f [服務名]"
    echo "   重啟服務:   docker-compose restart [服務名]"
    echo "   停止服務:   docker-compose down"
    echo "   更新系統:   docker-compose pull && docker-compose up -d"
    echo ""
    echo "📚 更多信息請查看 COMPLETE_README.md"
    echo ""
}

# 主要部署流程
main() {
    echo "開始自動部署流程..."
    echo ""
    
    # 檢查並提示用戶
    read -p "是否繼續部署？(Y/n): " confirm
    if [[ $confirm == "n" || $confirm == "N" ]]; then
        echo "部署已取消"
        exit 0
    fi
    
    # 執行部署步驟
    check_requirements
    setup_directories
    setup_environment
    setup_python_env
    download_models
    build_docker
    start_services
    health_check
    show_deployment_info
    
    echo "🎊 恭喜！AI營銷內容生成系統部署成功！"
}

# 錯誤處理
trap 'echo "❌ 部署過程中發生錯誤，請檢查上述輸出"; exit 1' ERR

# 執行主流程
main "$@"