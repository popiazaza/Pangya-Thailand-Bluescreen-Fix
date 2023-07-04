@echo off
title Pangya Thailand Bluescreen Fix 1.00
echo ===== Pangya Thailand Bluescreen Fix 1.00 =====
echo Checking if mitmdump is installed...
call mitmdump --version >nul 2>&1
if %errorlevel% neq 0 (
    echo mitmdump not found, please install mitmproxy
    echo https://mitmproxy.org/
    echo.
    pause
    exit /b
)
echo Starting Pangya Bypass Proxy...
echo Press CTRL+C to stop
start "PangyaBypassProxy" "mitmdump"  -s proxy.py