@echo off
set port=%1
IF "%port%" == "" ( set port=55555 )

".\platform-tools\adb.exe" kill-server
".\platform-tools\adb.exe" connect localhost:%port%
cd .\
pip install -r requirements.txt
python roktracker_1509.py

PAUSE