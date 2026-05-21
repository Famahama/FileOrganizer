@echo off
set "FOLDER=%~dp0"
if "%FOLDER:~-1%"=="\" set "FOLDER=%FOLDER:~0,-1%"

set "CACHE_DIR=%LOCALAPPDATA%\ProgresifTools"
set "CACHE=%CACHE_DIR%\reorganise.py"
set "URL=https://raw.githubusercontent.com/Famahama/FileOrganizer/main/reorganise.py"

:: Create cache folder and try to pull latest version (silent, 5s timeout)
powershell -NoProfile -Command "$null = New-Item -ItemType Directory -Force '%CACHE_DIR%'; try { Invoke-WebRequest -Uri '%URL%' -OutFile '%CACHE%' -UseBasicParsing -TimeoutSec 5 } catch {}" >nul 2>&1

:: Run from cache, or warn if never downloaded
if exist "%CACHE%" (
    python "%CACHE%" "%FOLDER%"
) else (
    echo.
    echo  Could not load the tool.
    echo  Check your internet connection and try again.
    echo.
    pause
)
