''' 
the source code for VirboxQuest
''' 
from json import loads, dumps
from os import getlogin, mkdir
from os.path import isfile
import sys
from random import randint

CPATH = f"/home/{getlogin()}/.config/VirboxQuest/data.json"
CONFIG = {"boxcoins": 0, "levels_completed": 0, "items_owned": []}
STORE = {"VIM_MANUAL": ["Vim Cheatsheet", "A simple cheatsheet for vim", 10], "ANTI_GRASS": ["Grass Avoider", "A tool to help from avoiding grass", 100]} 
DEF_POS = int(0)
USER_POS = 0

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
    print("Since Microssia invaded Gkaine... Many vim users are sent into the grasslands of Micsow..")
    print("Welcome fellow traveller.. you are currently in Editoria and now you have to go through a series of adventures to find Virbox...")

def level_1():
    global USER_POS
    print("\x1b[36m!\x1b[0m you are in the neighbourhood of Viev.. now go through 4 houses and find the vim guy")
    l1_map = '''\x1b[34m!\x1b[0m map for this level:
    |1|
    |2|
    |3|
    |4|
    |5|
    |6|
    |7|
    |8|
    |9|
  --10|
  | 11| 
  --12|
   |13|
   |14|
   |15--|
   |16  |
   |17--|
  --18|
  | 19|
  --20--
   |21 |
  |22 --
    '''
    VIM_USER = randint(1, 4)
    H1 = 11
    H2 = 16
    H3 = 19
    H4 = 22
    VISIT_H1 = False
    VISIT_H2 = False
    VISIT_H3 = False
    VISIT_H4 = False
    VIM_UH = None
    
    if VIM_USER == 1:
        VIM_UH = 11
    elif VIM_USER == 2:
        VIM_UH = 16
    elif VIM_USER == 3:
        VIM_UH = 19
    else:
        VIM_UH = 22

    while True:
        choice = input("\x1b[32m>\x1b[0m command: ")
        if choice == "help":
            print("\x1b[34mmap\x1b[0m: view map\n\x1b[34mback\x1b[0m: move back\n\x1b[34mfront\x1b[0m: move forward\n\x1b[34mhelp\x1b[0m: show this menu\n\x1b[34mchest\x1b[0m: view stuff\n\x1b[34mstore\x1b[0m: buy items")
        elif choice == "store":
            store()
        elif choice == "exit":
            exit_game()
        elif choice == "chest":
            chest()
        elif choice == "front":
            if USER_POS >= 25:
                print("\x1b[33m!\x1b[0m end of world")
            elif USER_POS == 11 and VIM_UH == 11 and VISIT_H1 == False or USER_POS == 16 and VIM_UH == 16 and VISIT_H2 == False or USER_POS == 19 and VIM_UH == 19 and VISIT_H3 == False or USER_POS == 22 and VIM_UH == 22 and VISIT_H4 == False:
                print("\x1b[32m!\x1b[0m you found the vim user... + 10 boxcoins")
                print("\x1b[32m!\x1b[0m congrats level 1 passed")
                break
            else:
                USER_POS = USER_POS+1
        elif choice == "map":
            print(l1_map)
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
