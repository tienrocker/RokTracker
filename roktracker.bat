@echo off
set port=%1
IF "%port%" == "" ( set port=55555 )

netstat -o -n -a | findstr %port%

if %ERRORLEVEL% equ 0 (
    ".\platform-tools\adb.exe" kill-server
    ".\platform-tools\adb.exe" connect localhost:%port%
    cd .\
    pip install -r requirements.txt
    python roktracker.py
) else (
    echo "PORT %port% not open"
)

PAUSE