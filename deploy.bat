@echo off
:: AI營銷內容生成系統 - Windows快速部署腳本

echo 🚀 AI營銷內容生成系統 - 自動部署開始
echo ==================================================

:: 檢查Docker Desktop
echo 📋 檢查Docker Desktop...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 錯誤: 未找到Docker Desktop
    echo 請先安裝並啟動Docker Desktop
    echo 下載地址: https://desktop.docker.com/win/main/amd64/Docker Desktop Installer.exe
    pause
    exit /b 1
)

echo ✅ Docker已安裝: 
docker --version

:: 檢查Docker Desktop是否運行
echo 📋 檢查Docker Desktop運行狀態...
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker Desktop未運行
    echo 正在嘗試啟動Docker Desktop...
    start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    echo 請等待Docker Desktop啟動完成後重新運行此腳本
    pause
    exit /b 1
)

echo ✅ Docker Desktop運行正常

REM 檢查系統要求
echo 📋 檢查系統要求...

REM 檢查Python
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ❌ 錯誤: 未找到Python
    echo 請安裝Python 3.9-3.11版本
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python版本: %PYTHON_VERSION%

REM 檢查Docker Desktop
docker --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ❌ 錯誤: 未找到Docker
    echo 請安裝Docker Desktop
    pause
    exit /b 1
)

docker --version
echo ✅ Docker已安裝

REM 檢查Docker Compose
docker-compose --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ❌ 錯誤: 未找到Docker Compose
    echo 請安裝Docker Desktop 2.0+
    pause
    exit /b 1
)

docker-compose --version
echo ✅ Docker Compose已安裝

REM 檢查NVIDIA GPU
nvidia-smi >nul 2>&1
if %errorLevel% equ 0 (
    echo ✅ 檢測到NVIDIA GPU:
    nvidia-smi --query-gpu=name,memory.total --format=csv,noheader,nounits | head -1
) else (
    echo ⚠️  未檢測到NVIDIA GPU，將使用CPU模式
    echo    建議使用RTX 3090或更高級別的GPU以獲得最佳性能
)

REM 創建必要目錄
echo 📁 創建項目目錄...
if not exist "checkpoints" mkdir checkpoints
if not exist "uploads" mkdir uploads
if not exist "outputs" mkdir outputs
if not exist "outputs\images" mkdir outputs\images
if not exist "outputs\videos" mkdir outputs\videos
if not exist "outputs\text" mkdir outputs\text
if not exist "logs" mkdir logs
if not exist "data" mkdir data

echo ✅ 項目目錄已創建

REM 設置環境配置
echo ⚙️  設置環境配置...
if not exist ".env" (
    copy ".env.example" ".env" >nul
    echo ✅ 已創建 .env 配置文件
    echo 📝 請編輯 .env 文件設置必要的配置項：
    echo    - POSTGRES_PASSWORD ^(數據庫密碼^)
    echo    - JWT_SECRET_KEY ^(JWT密鑰^)
    echo    - HUGGINGFACE_TOKEN ^(可選，用於下載模型^)
    echo.
    set /p edit_config="是否現在編輯配置文件？(y/N): "
    if /i "%edit_config%"=="y" (
        notepad .env
    )
) else (
    echo ✅ 環境配置文件已存在
)

REM 創建Python虛擬環境
echo 🐍 設置Python虛擬環境...
if not exist "ai_marketing_env" (
    python -m venv ai_marketing_env
    echo ✅ 虛擬環境已創建
)

call ai_marketing_env\Scripts\activate.bat
echo ✅ 虛擬環境已激活

REM 升級pip
python -m pip install --upgrade pip

REM 安裝PyTorch
echo 📦 安裝PyTorch...
nvidia-smi >nul 2>&1
if %errorLevel% equ 0 (
    pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 torchaudio==2.1.2+cu118 -f https://download.pytorch.org/whl/torch_stable.html
    echo ✅ 已安裝CUDA版PyTorch
) else (
    pip install torch torchvision torchaudio
    echo ✅ 已安裝CPU版PyTorch
)

REM 安裝項目依賴
echo 📦 安裝項目依賴...
pip install -r requirements\pt2.txt

REM 安裝額外依賴
pip install fastapi uvicorn sqlalchemy psycopg2-binary redis celery gradio
pip install transformers diffusers accelerate xformers
pip install matplotlib plotly pandas requests pillow

echo ✅ 所有依賴已安裝完成

REM 下載AI模型
echo 🤖 下載AI模型...
echo ⚠️  注意: 模型總大小約50GB，請確保有足夠的網絡和存儲空間

set /p download_confirm="是否開始下載模型？(Y/n): "
if /i "%download_confirm%"=="n" (
    echo ⏭️  跳過模型下載，稍後可手動運行: python download_models.py
) else (
    python download_models.py
    echo ✅ 模型下載完成
)

REM 構建Docker鏡像
echo 🐳 構建Docker鏡像...
docker-compose build --parallel
if %errorLevel% neq 0 (
    echo ❌ Docker鏡像構建失敗
    pause
    exit /b 1
)
echo ✅ Docker鏡像構建完成

REM 啟動服務
echo 🚀 啟動服務...

echo    啟動數據庫和緩存服務...
docker-compose up -d postgres redis

echo    等待數據庫啟動...
timeout /t 15 /nobreak >nul

echo    啟動AI生成服務...
docker-compose up -d ai-generator celery-worker

echo    啟動Web界面...
docker-compose up -d gradio-interface

echo    啟動監控服務...
docker-compose up -d nginx prometheus grafana

echo ✅ 所有服務已啟動

REM 健康檢查
echo 🔍 執行健康檢查...
timeout /t 30 /nobreak >nul

REM 檢查API服務
curl -f http://localhost:8000/health >nul 2>&1
if %errorLevel% equ 0 (
    echo ✅ API服務運行正常
) else (
    echo ❌ API服務異常，請檢查Docker日志
)

REM 檢查Web界面
curl -f http://localhost:7860 >nul 2>&1
if %errorLevel% equ 0 (
    echo ✅ Web界面運行正常
) else (
    echo ❌ Web界面異常，請檢查Docker日志
)

echo ✅ 健康檢查完成

REM 顯示部署信息
echo.
echo 🎉 部署完成！系統已啟動並運行
echo ==================================================
echo.
echo 🌐 訪問地址:
echo    Web界面:    http://localhost:7860
echo    API服務:    http://localhost:8000
echo    API文檔:    http://localhost:8000/docs
echo    監控面板:   http://localhost:3000 ^(admin/admin^)
echo.
echo 📊 服務狀態:
docker-compose ps
echo.
echo 🛠️  常用命令:
echo    查看日志:   docker-compose logs -f [服務名]
echo    重啟服務:   docker-compose restart [服務名]
echo    停止服務:   docker-compose down
echo    更新系統:   docker-compose pull ^&^& docker-compose up -d
echo.
echo 📚 更多信息請查看 COMPLETE_README.md
echo.
echo 🎊 恭喜！AI營銷內容生成系統部署成功！

pause