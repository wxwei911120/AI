@echo off
:: AI營銷內容生成系統 - 修復版部署腳本
chcp 65001 >nul

echo 🚀 AI營銷內容生成系統 - Docker修復版
echo ==================================================

echo 🔧 Docker問題診斷和修復...

:: 檢查Docker Desktop是否安裝
where docker >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker未安裝，請安裝Docker Desktop
    echo 下載: https://desktop.docker.com/win/main/amd64/Docker Desktop Installer.exe
    pause
    exit /b 1
)

echo ✅ Docker已安裝

:: 嘗試修復Docker連接問題
echo 🔄 檢查並修復Docker服務...
docker version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Docker API連接錯誤，正在修復...
    
    :: 重啟Docker Desktop
    echo    停止Docker Desktop...
    taskkill /f /im "Docker Desktop.exe" >nul 2>&1
    wsl --shutdown >nul 2>&1
    timeout /t 10 /nobreak >nul
    
    echo    重新啟動Docker Desktop...
    start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    timeout /t 30 /nobreak >nul
    
    :: 再次檢查
    docker version >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ Docker修復失敗，使用備用方案
        goto :fallback_mode
    )
)

echo ✅ Docker服務正常

:: 選擇部署模式
echo.
echo 📋 選擇部署模式：
echo 1. GPU版本 (推薦，需要NVIDIA GPU)
echo 2. CPU版本 (通用，較慢但穩定) 
echo 3. Python直接運行 (最快啟動)
echo.
set /p mode="請選擇模式 (1-3): "

if "%mode%"=="1" goto :gpu_mode
if "%mode%"=="2" goto :cpu_mode  
if "%mode%"=="3" goto :python_mode
goto :cpu_mode

:gpu_mode
echo 🎮 使用GPU版本部署...
echo    檢查NVIDIA GPU...
nvidia-smi >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  未檢測到NVIDIA GPU，切換到CPU模式
    goto :cpu_mode
)
echo    修復Dockerfile...
echo FROM nvidia/cuda:11.8-devel-ubuntu22.04 > Dockerfile.fixed
echo. >> Dockerfile.fixed
type Dockerfile | findstr /v "FROM nvidia/cuda:11.8-cudnn8-devel-ubuntu22.04" >> Dockerfile.fixed
move Dockerfile.fixed Dockerfile >nul

echo    停止現有服務...
docker-compose down >nul 2>&1

echo    構建並啟動GPU版本...
docker-compose up -d --build
goto :check_status

:cpu_mode
echo 💻 使用CPU版本部署...
echo    停止現有服務...
docker-compose -f docker-compose.cpu.yml down >nul 2>&1

echo    構建並啟動CPU版本...
docker-compose -f docker-compose.cpu.yml up -d --build
goto :check_status

:python_mode
echo 🐍 使用Python直接運行模式...
if not exist "outputs" mkdir outputs
if not exist "outputs\images" mkdir outputs\images  
if not exist "outputs\videos" mkdir outputs\videos
if not exist "outputs\text" mkdir outputs\text

echo    安裝必要依賴...
pip install plotly diffusers accelerate >nul 2>&1

echo    啟動系統...
start /b python python_launcher.py
timeout /t 15 /nobreak >nul
goto :python_status

:fallback_mode  
echo 💡 Docker無法修復，使用Python備用模式...
goto :python_mode

:check_status
echo ⏳ 等待服務啟動...
timeout /t 30 /nobreak >nul

echo 🔍 檢查服務狀態...
docker-compose ps 2>nul || docker-compose -f docker-compose.cpu.yml ps 2>nul

echo 🌐 測試服務連接...
curl -s http://localhost:7860 >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Web界面正常: http://localhost:7860
) else (
    echo ⚠️  Web界面啟動中，請稍候再試
)

curl -s http://localhost:8000/health >nul 2>&1  
if %errorlevel% equ 0 (
    echo ✅ API服務正常: http://localhost:8000
) else (
    echo ⚠️  API服務啟動中，請稍候再試
)
goto :finish

:python_status
curl -s http://localhost:7860 >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ 系統啟動成功: http://localhost:7860
) else (
    echo ⚠️  系統啟動中，請稍候再試: http://localhost:7860
)

:finish
echo.
echo 🎉 部署完成！
echo ==================================================
echo.
echo 🌐 訪問地址:
echo    Web界面: http://localhost:7860  
echo    API服務: http://localhost:8000
echo    API文檔: http://localhost:8000/docs
echo.
echo 🛠️  如果無法訪問，請等待1-2分鐘後重試
echo    或運行: docker-compose logs -f gradio-interface
echo.
echo 🔧 故障排除:
echo    1. 確保防火牆未阻擋端口7860和8000
echo    2. 檢查其他程序是否佔用端口
echo    3. 重新運行此腳本選擇不同模式
echo.

pause