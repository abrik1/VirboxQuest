'''
the source code for VirboxQuest
'''
from json import loads, dumps
from os import getlogin, mkdir
from os.path import isfile
import sys

cpath = f"/home/{getlogin()}/.config/VirboxQuest/data.json"
config = {"boxcoins": 0, "levels_completed": 0}

def check_config():
    '''
    This function checks config file
    '''
    if isfile(cpath) == True:
        return True
    else:
        try:
            mkdir(f"/home/{getlogin()}/.config/VirboxQuest/")
        except FileExistsError:
            config_file = open(cpath, 'w')
            config_file.write(str(dumps(config)))
            config_file.close()
            return True
        
        config_file = open(cpath, 'w')
        config_file.write(str(dumps(config)))
        config_file.close()
        return True

def parse_config():
    global config
    '''
    This function parses config file
    '''
    with open(cpath, 'r', encoding="utf-8") as config_file:
        config_data = loads(config_file.read())
    config_file.close()

    if "boxcoins" and "levels_completed" in list(config_data.keys()):
        config["boxcoins"] = config_data["boxcoins"]
        config["levels_completed"] = config_data["levels_completed"]
    else:
        print("\x1b[31m!\x1b[0m config error..")
        sys.exit(1)
        
    
if __name__ == "__main__":
    check_config()
    parse_config()
