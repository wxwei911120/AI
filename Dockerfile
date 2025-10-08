# Docker配置文件
# AI行銷內容生成系統 - 完整版

FROM nvidia/cuda:11.8-devel-ubuntu22.04

# 設置環境變數
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV CUDA_VISIBLE_DEVICES=0

# 設置工作目錄
WORKDIR /app

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3.10-dev \
    python3-pip \
    git \
    wget \
    curl \
    unzip \
    ffmpeg \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# 升級pip
RUN python3 -m pip install --upgrade pip

# 複製需求文件
COPY requirements_full.txt /app/

# 安裝Python依賴
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip install -r requirements_full.txt

# 複製專案文件
COPY . /app/

# 創建必要目錄
RUN mkdir -p /app/outputs/text /app/outputs/images /app/outputs/videos
RUN mkdir -p /app/checkpoints
RUN mkdir -p /app/logs

# 設置權限
RUN chmod +x /app/marketing_content_generator/*.py

# 暴露端口
EXPOSE 7860 8000

# 創建啟動腳本
RUN echo '#!/bin/bash\n\
echo "🚀 啟動AI行銷內容生成系統..."\n\
echo "GPU信息:"\n\
nvidia-smi\n\
echo "\n開始下載模型..."\n\
python3 /app/download_models.py\n\
echo "\n啟動Web界面..."\n\
cd /app/marketing_content_generator\n\
python3 gradio_interface_full.py\n\
' > /app/start.sh && chmod +x /app/start.sh

# 健康檢查
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:7860/health || exit 1

# 啟動命令
CMD ["/app/start.sh"]