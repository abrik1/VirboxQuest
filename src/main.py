'''
the source code for VirboxQuest
'''
from json import loads, dumps
from os import getlogin, mkdir
from os.path import isfile
import sys

CPATH = f"/home/{getlogin()}/.config/VirboxQuest/data.json"
CONFIG = {"boxcoins": 0, "levels_completed": 0}

def check_config():
    '''
    This function checks config file
    '''
    if isfile(CPATH):
        pass
    else:
        try:
            mkdir(f"/home/{getlogin()}/.config/VirboxQuest/")
        except FileExistsError:
            with open(CPATH, 'w', encoding="utf-8") as config_file:
                config_file.write(str(dumps(CONFIG)))
            config_file.close()

        with open(CPATH, 'w', encoding="utf-8") as config_file:
            config_file.write(str(dumps(CONFIG)))
        config_file.close()

def parse_config():
    '''
    This function parses config file
    '''
    with open(CPATH, 'r', encoding="utf-8") as config_file:
        config_data = loads(config_file.read())
    config_file.close()

    if "levels_completed" in list(config_data.keys()):
        CONFIG["boxcoins"] = config_data["boxcoins"]
        CONFIG["levels_completed"] = config_data["levels_completed"]
    else:
        print("\x1b[31m!\x1b[0m config error..")
        sys.exit(1)
if __name__ == "__main__":
    check_config()
    parse_config()
