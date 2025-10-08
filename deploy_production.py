#!/usr/bin/env python3
"""
AI Marketing Content Generation System - Production Deployment Script
適合雲服務器和生產環境的部署腳本
"""

import os
import sys
import subprocess
import signal
import logging
from pathlib import Path

# 配置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('deployment.log'),
        logging.StreamHandler()
    ]
)

class ProductionDeployment:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.requirements_file = self.project_root / "requirements_full.txt"
        self.main_app = self.project_root / "ultimate_launcher.py"
        
    def check_environment(self):
        """檢查運行環境"""
        logging.info("檢查系統環境...")
        
        # 檢查Python版本
        python_version = sys.version_info
        if python_version.major != 3 or python_version.minor < 8:
            logging.error(f"需要Python 3.8+，當前版本: {sys.version}")
            return False
            
        # 檢查磁盤空間（需要至少20GB）
        import shutil
        free_space = shutil.disk_usage(self.project_root).free / (1024**3)
        if free_space < 20:
            logging.error(f"磁盤空間不足，需要至少20GB，當前可用: {free_space:.1f}GB")
            return False
            
        logging.info(f"環境檢查通過 - Python {sys.version}, 可用空間: {free_space:.1f}GB")
        return True
        
    def install_dependencies(self):
        """安裝依賴項"""
        logging.info("安裝系統依賴...")
        
        try:
            # 升級pip
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                         check=True, capture_output=True)
            
            # 安裝requirements
            if self.requirements_file.exists():
                subprocess.run([sys.executable, "-m", "pip", "install", "-r", 
                             str(self.requirements_file)], check=True, capture_output=True)
            
            # 安裝生產環境需要的額外包
            production_packages = [
                "gunicorn",      # WSGI服務器
                "nginx",         # 可選：nginx配置
                "certbot",       # SSL證書
                "supervisor",    # 進程管理
                "redis",         # 快取（可選）
            ]
            
            for package in production_packages:
                try:
                    subprocess.run([sys.executable, "-m", "pip", "install", package], 
                                 check=True, capture_output=True)
                    logging.info(f"已安裝: {package}")
                except subprocess.CalledProcessError:
                    logging.warning(f"無法安裝: {package} (可選)")
            
            return True
            
        except subprocess.CalledProcessError as e:
            logging.error(f"依賴安裝失敗: {e}")
            return False
    
    def create_systemd_service(self):
        """創建systemd服務文件（Linux）"""
        service_content = f"""[Unit]
Description=AI Marketing Content Generation System
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory={self.project_root}
ExecStart={sys.executable} {self.main_app}
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=ai-marketing
Environment=PYTHONPATH={self.project_root}

[Install]
WantedBy=multi-user.target
"""
        
        service_file = Path("/etc/systemd/system/ai-marketing.service")
        try:
            with open(service_file, 'w') as f:
                f.write(service_content)
            logging.info(f"創建systemd服務文件: {service_file}")
            
            # 啟用服務
            subprocess.run(["systemctl", "enable", "ai-marketing"], check=True)
            subprocess.run(["systemctl", "daemon-reload"], check=True)
            
            return True
        except (PermissionError, subprocess.CalledProcessError) as e:
            logging.error(f"創建systemd服務失敗: {e}")
            return False
    
    def create_nginx_config(self):
        """創建Nginx配置"""
        nginx_config = """server {
    listen 80;
    server_name your-domain.com;  # 替換為你的域名
    
    # 重定向到HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;  # 替換為你的域名
    
    # SSL配置
    ssl_certificate /path/to/your/certificate.crt;
    ssl_certificate_key /path/to/your/private.key;
    
    # 安全標頭
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
    
    # 代理到Gradio應用
    location / {
        proxy_pass http://127.0.0.1:7861;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # 增加超時設置
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
        
        # 文件上傳大小限制
        client_max_body_size 100M;
    }
    
    # 靜態文件快取
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}"""
        
        nginx_file = self.project_root / "nginx_ai_marketing.conf"
        with open(nginx_file, 'w') as f:
            f.write(nginx_config)
            
        logging.info(f"創建Nginx配置文件: {nginx_file}")
        logging.info("請將此文件複製到 /etc/nginx/sites-available/ 並啟用")
        
    def create_docker_production(self):
        """創建生產環境Docker配置"""
        dockerfile_prod = """FROM python:3.10-slim

# 設置工作目錄
WORKDIR /app

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 複製項目文件
COPY . /app/

# 安裝Python依賴
RUN pip install --no-cache-dir -r requirements_full.txt

# 創建必要目錄
RUN mkdir -p /app/outputs/images /app/outputs/videos /app/outputs/text

# 設置權限
RUN chmod +x /app/ultimate_launcher.py

# 暴露端口
EXPOSE 7861

# 健康檢查
HEALTHCHECK --interval=30s --timeout=30s --start-period=60s --retries=3 \
  CMD curl -f http://localhost:7861/ || exit 1

# 啟動應用
CMD ["python", "ultimate_launcher.py"]
"""
        
        dockerfile_path = self.project_root / "Dockerfile.production"
        with open(dockerfile_path, 'w') as f:
            f.write(dockerfile_prod)
            
        # Docker Compose生產配置
        docker_compose_prod = """version: '3.8'

services:
  ai-marketing:
    build:
      context: .
      dockerfile: Dockerfile.production
    ports:
      - "7861:7861"
    volumes:
      - ./outputs:/app/outputs
      - ./checkpoints:/app/checkpoints
    environment:
      - GRADIO_SERVER_NAME=0.0.0.0
      - GRADIO_SERVER_PORT=7861
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 8G
          cpus: '4.0'
        reservations:
          memory: 4G
          cpus: '2.0'
    
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx_ai_marketing.conf:/etc/nginx/conf.d/default.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - ai-marketing
    restart: unless-stopped

  redis:
    image: redis:alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data

volumes:
  redis_data:
"""
        
        compose_path = self.project_root / "docker-compose.production.yml"
        with open(compose_path, 'w') as f:
            f.write(docker_compose_prod)
            
        logging.info(f"創建生產環境Docker文件: {dockerfile_path}")
        logging.info(f"創建生產環境Docker Compose: {compose_path}")
    
    def deploy(self):
        """執行完整部署流程"""
        logging.info("開始生產環境部署...")
        
        if not self.check_environment():
            logging.error("環境檢查失敗，部署中止")
            return False
            
        if not self.install_dependencies():
            logging.error("依賴安裝失敗，部署中止")
            return False
            
        # 創建配置文件
        self.create_nginx_config()
        self.create_docker_production()
        
        # Linux系統創建systemd服務
        if sys.platform.startswith('linux'):
            self.create_systemd_service()
            
        logging.info("=" * 60)
        logging.info("部署完成！接下來的步驟：")
        logging.info("")
        logging.info("1. 雲服務器部署:")
        logging.info("   python deploy_production.py")
        logging.info("")
        logging.info("2. Docker部署:")
        logging.info("   docker-compose -f docker-compose.production.yml up -d")
        logging.info("")
        logging.info("3. 設置域名和SSL:")
        logging.info("   - 配置DNS指向服務器IP")
        logging.info("   - 安裝SSL證書 (Let's Encrypt)")
        logging.info("   - 修改nginx配置中的域名")
        logging.info("")
        logging.info("4. 防火牆設置:")
        logging.info("   sudo ufw allow 80")
        logging.info("   sudo ufw allow 443")
        logging.info("   sudo ufw allow 7861")
        logging.info("")
        logging.info("5. 啟動服務:")
        logging.info("   sudo systemctl start ai-marketing")
        logging.info("   sudo systemctl start nginx")
        logging.info("=" * 60)
        
        return True

def main():
    """主函數"""
    deployment = ProductionDeployment()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--run-app":
        # 直接運行應用
        logging.info("直接啟動AI營銷系統...")
        os.system(f"python {deployment.main_app}")
    else:
        # 執行完整部署
        deployment.deploy()

if __name__ == "__main__":
    main()