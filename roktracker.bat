".\platform-tools\adb.exe" kill-server
".\platform-tools\adb.exe" connect localhost:61325
cd .\
pip install -r requirements.txt
python roktracker.py
PAUSE