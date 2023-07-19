'''
the source code for VirboxQuest
'''

from json import loads, dumps
from os import getlogin, mkdir
from os.path import isfile

cpath = f"/home/{getlogin()}/.config/VirboxQuest/data.json"

def check_config():
    if isfile(cpath) == True:
        return 0
    else:
        try:
            mkdir(f"/home/{getlogin()}/.config/VirboxQuest/")
        except FileExistsError:
            with open(cpath, 'w', encoding="utf-8") as config:
                config.write('')
                
            config.close()
            return 0

        with open(cpath, 'w', encoding="utf-8") as config:
            config.write()
                
        config.close()
        return 0
        

if __name__ == "__main__":
    check_config()
