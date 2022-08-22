".\platform-tools\adb.exe" kill-server
".\platform-tools\adb.exe" connect localhost:53256
cd .\
pip install -r requirements.txt
python roktracker.py
PAUSE