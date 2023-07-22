''' 
the source code for VirboxQuest
''' 
from json import loads, dumps
from os import getlogin, mkdir
from os.path import isfile
import sys

CPATH = f"/home/{getlogin()}/.config/VirboxQuest/data.json"
CONFIG = {"boxcoins": 0, "levels_completed": 0, "items_owned": []}
STORE = {"VIM_MANUAL": ["Vim Cheatsheet", "A simple cheatsheet for vim", 10], "ANTI_GRASS": ["Grass Avoider", "A tool to help from avoiding grass", 100]} 

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
        CONFIG["items_owned"] = config_data["items_owned"]
    else:
        print("\x1b[31m!\x1b[0m config error..")
        sys.exit(1)

def chest():
    while True:
        store_choice = input("\x1b[32m> \x1b[35mchest\x1b[0m: ")
        if store_choice == "help":
            print("\x1b[34mlist\x1b[0m: list items in chest\n\x1b[34mhelp\x1b[0m: show this menu\n\x1b[34mexit\x1b[0m: exit store mode")
        elif store_choice == "exit":
            break
        elif store_choice == "list":
            print("\x1b[36m!\x1b[0m items in chest:")
            for i in range(0, len(CONFIG['items_owned'])):
                print(f"\x1b[36m{i+1} \x1b[34m{CONFIG['items_owned'][i]}\x1b[0m")
        else:
            print("\x1b[31m!\x1b[0m invalid choice")
        
def store():
    while True:
        store_choice = input("\x1b[32m> \x1b[35mstore\x1b[0m: ")
        if store_choice == "help":
            print("\x1b[34mbuy\x1b[0m: buy an item\n\x1b[34mlist\x1b[0m: list available items\n\x1b[34mhelp\x1b[0m: show this menu")
        elif store_choice == "list":
            print("\x1b[36m!\x1b[0m available items:")
            a = []
            for i in range(0, len(list(STORE.keys()))):
                print(f"\x1b[36m{i+1}\x1b[0m {STORE[list(STORE.keys())[i]][0]}\x1b[33m {STORE[list(STORE.keys())[i]][2]} - Boxcoins\x1b[0m")
        elif store_choice == "exit":
            break
        elif store_choice == "buy":
            name = []
            boxc_val = []
            for i in range(0, len(list(STORE.keys()))):
                name.append(STORE[list(STORE.keys())[i]][0])
                boxc_val.append(STORE[list(STORE.keys())[i]][2])
                print(f"\x1b[36m{i+1}\x1b[0m {STORE[list(STORE.keys())[i]][0]}\x1b[33m {STORE[list(STORE.keys())[i]][2]} - Boxcoins\x1b[0m")
            try:
                is_int = True
                choice = int(input("\x1b[34m?\x1b[0m please enter the item's number: "))
            except ValueError:
                is_int = False
                print("\x1b[31m!\x1b[0m please enter an integer")

            if is_int == True:            
                if choice > len(boxc_val):
                    print("\x1b[31m!\x1b[0m invalid choice")
                else:
                    if CONFIG['boxcoins'] >= boxc_val[choice-1]:
                        if name[choice-1] in CONFIG['items_owned']:
                            print(f"\x1b[33m!\x1b[0m {name[choice-1]} in chest already..")
                            pass
                        else:
                            print(f"\x1b[32m✓\x1b[0m {name[choice-1]} purchased")
                            CONFIG['boxcoins'] = CONFIG['boxcoins'] - boxc_val[choice-1]
                            CONFIG['items_owned'].append(name[choice-1])
                    else:
                        print(f"\x1b[31m!\x1b[0m sorry, you cannot afford {name[choice-1]}")
            else:
                pass
        else:
            print("\x1b[31m!\x1b[0m invalid choice")
        
def startup():
    print("Welcome to VirboxQuest...\nin this game of adventure you will be travelling through the world of Editoria... where people fight for editors...\n")
    print("In this game you will face adventures to save a vim user \"Virbox\" is kidnapped by some VSC newbie.. you need to save him...\n")

def level_1():
    print("\x1b[36m!\x1b[0m knowing the basics of vim... go to the house of \"Vim Diesel\"")
    while True:
        choice = input("\x1b[32m>\x1b[0m command: ")
        if choice == "help":
            print("\x1b[34mmap\x1b[0m: view map\n\x1b[34mleft\x1b[0m: move left\n\x1b[34mback\x1b[0m: move back\n\x1b[34mfront\x1b[0m: move forward\n\x1b[34mhelp\x1b[0m: show this menu\n\x1b[34mchest\x1b[0m: view stuff\n\x1b[34mstore\x1b[0m: buy items")
        elif choice == "store":
            store()
        elif choice == "exit":
            exit_game()
        elif choice == "chest":
            chest()
        else:
            print("\x1b[31m!\x1b[0m invalid choice")

def exit_game():
    with open(CPATH, 'w', encoding="utf-8") as config_save:
        config_save.write(str(dumps(CONFIG)))
    config_save.close()
    exit()
            
try:
    if __name__ == "__main__":
        check_config()
        parse_config()
        level_1()
except KeyboardInterrupt:
    print()
