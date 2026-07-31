@echo off
chcp 65001 >nul
cd /d "%~dp0"

where uv >nul 2>nul
if errorlevel 1 (
    echo [!] uv is not installed.
    pause
    exit /b 1
)

echo [*] Syncing dependencies...
uv sync

echo [*] Starting server at http://127.0.0.1:5000
uv run python src/main.py

pause
