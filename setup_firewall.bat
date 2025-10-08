@echo off
echo ================================================
echo AI營銷系統 - Windows防火牆配置工具
echo ================================================
echo.
echo 正在配置Windows防火牆...
echo 允許端口7861的入站和出站連接
echo.

REM 添加入站規則
netsh advfirewall firewall add rule name="AI Marketing Inbound 7861" dir=in action=allow protocol=TCP localport=7861
if %ERRORLEVEL% EQU 0 (
    echo ✅ 入站規則已添加
) else (
    echo ❌ 入站規則添加失敗 - 需要管理員權限
)

REM 添加出站規則
netsh advfirewall firewall add rule name="AI Marketing Outbound 7861" dir=out action=allow protocol=TCP localport=7861
if %ERRORLEVEL% EQU 0 (
    echo ✅ 出站規則已添加
) else (
    echo ❌ 出站規則添加失敗 - 需要管理員權限
)

echo.
echo ================================================
echo 防火牆配置完成！
echo.
echo 接下來需要檢查：
echo 1. 路由器端口轉發設置 (7861端口)
echo 2. ISP是否封鎖該端口
echo 3. 網絡運營商政策
echo ================================================
echo.
pause