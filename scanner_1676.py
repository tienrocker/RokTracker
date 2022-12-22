import os
import configparser
dummy = "TIENTM"

with open('C:\\ProgramData\\BlueStacks_nxt\\bluestacks.conf') as f:
    file_content = '['+dummy+']\n' + f.read()

config_parser = configparser.RawConfigParser()
config_parser.read_string(file_content)

for key, value in config_parser.items(dummy):
    if value == '"Scan"':
        key_port = key.replace("display_name", "status.adb_port")
        port = config_parser.get(dummy, key_port)
        # print(port)
        os.system(".\\roktracker_1676.bat " + port)

os.system("")
