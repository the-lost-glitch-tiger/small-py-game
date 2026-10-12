
import os
import pickle
import time
import signal
import sys
import random

from funcs import get_key

#import keyboard
from colorama import Fore, Back, Style

game_loc = './sPyGame'
game_save_path = 'saves'

default_config = {
    "text_speed": 10
    }

if os.path.exists(game_loc+'/config.pkl') == False:
    if os.path.exists(game_loc) == False:
        os.mkdir(game_loc)
    with open(game_loc+'/config.pkl', 'wb') as f:
        pickle.dump(default_config, f)
elif os.path.exists(game_loc+'/config.pkl'):
    with open(game_loc+'/config.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)


SkillsDB = {
    "Basic Sword Attack": {
        "Name": "Basic Sword Attack",
        "base_DMG": 2,        
        },
    "Basic fast run": {
        "Name": "Basic fast run",
        "speed_Boost": 2,
        },
    "Lighting Strike": {
        "Name": "Lighting Strike",
        "base_DBG": 5,
    }
}


def main():
    print(Style.RESET_ALL)
    print('\n------------')
    print("Welcome! \n")
    try:
        while True:
            print("- - - - - -")
            print(Fore.BLUE + "REALMS")
            print(Fore.CYAN + "1. Realms")
            print(Fore.YELLOW + "2. Settings")
            print(Fore.RED + "0. Quit")
            print(Style.RESET_ALL)
            choice = input(Style.BRIGHT + "Path: ")
            print(Style.RESET_ALL)
            if choice == '0':
                break
            elif choice == '1':
                Realms()
            elif choice == '2':
                Settings()
            elif choice == "000":
                print("")
    except KeyboardInterrupt:
        print(Style.RESET_ALL)

def Realms():
    print(Fore.LIGHTBLUE_EX + "1. Load Realm")
    print(Fore.LIGHTGREEN_EX + "2. Create Realm")
    print(Fore.LIGHTCYAN_EX + "3. View Realms Data")
    print(Fore.LIGHTRED_EX + "0. Return")
    print(Style.RESET_ALL)
    choice = input(Style.BRIGHT + "Realms input: ")
    print(Style.RESET_ALL)
    if choice == '0':
        return
    elif choice == '1':
        RealmLoader()
    elif choice == '2':
        CreateRealm()
    elif choice == '3':
        realms_data_viewer()

def realms_data_viewer():
    print(f"Save folder: {os.path.abspath(game_save_path)}\n")
    Realms()
        
def RealmLoader():
    print('')
    odNum = 0
    try:
        dirfi = os.listdir(game_loc+'/'+game_save_path)
        print("# | Name | Last modification")
        for fin in dirfi:
            #print(os.path.basename(game_loc+'/'+game_save_path+'/'+fin))
            odNum += 1
            with open(game_loc+'/'+game_save_path+'/'+fin, 'rb') as f:
                loaded_dict = pickle.load(f)
                print(f"{odNum}. {loaded_dict['Name']} | {time.ctime(os.path.getmtime(game_loc+'/'+game_save_path+'/'+fin), )} |")
                #print(loaded_dict)
    except FileNotFoundError:
        print('No saves found.')
    print(Fore.LIGHTCYAN_EX + "\n1. Load world by name")
    #print("2. Load world by ID ") #Under work #Does not work for now
    print(Fore.RED + "0. Return")
    print(Style.RESET_ALL)
    choice = input(Style.BRIGHT + "Choose: ")
    print(Style.RESET_ALL)
    if choice == '0':
        return
    elif choice == '1':
        nml = input(Style.BRIGHT + "Enter Save Name: ")
        print(Style.RESET_ALL)
        try:
            with open(game_loc+'/'+game_save_path+'/'+nml+'.pkl', 'rb') as f:
                savef_dict = pickle.load(f)
                game_loop(savef_dict)
        except FileNotFoundError:
            print("Save does not exist")
    elif choice == '2':
        #nml = input("Enter Save Name: ")
        #with open(game_loc+'/'+game_save_path+'/'+nml+'.pkl', 'rb') as f:
            #savef_dict = pickle.load(f)
        pass
    

def CreateRealm():
    SaveName = input(Style.BRIGHT + "Enter Realm Name (savename): ")
    if len(SaveName) >= 2:
        pass
    else:
        print(Style.RESET_ALL)
        print("Too short!")
        return
    print(Style.RESET_ALL)
    RealmSaveF = {
        "Name": SaveName,
        "Player": {
            "Health": 100,
            "Max_Health": 100,
            "Skills": [
                SkillsDB["Basic Sword Attack"]
                ],
        },
    }
    #if os.path.exists()
    print("1. Confirm Realms Creation")
    print("2. Cancle")
    confirm = input(Style.BRIGHT + "Confirm (1 or 2): ")
    print(Style.RESET_ALL)
    if confirm == '1':
        if os.path.exists(game_loc+'/'+game_save_path+'/'+SaveName+'.pkl') == False:
            if os.path.exists(game_loc+'/'+game_save_path) == False:
                os.mkdir(game_loc+'/'+game_save_path)
            with open(game_loc+'/'+game_save_path+'/'+SaveName+'.pkl', 'wb') as f:
                pickle.dump(RealmSaveF, f)
        elif os.path.exists(game_loc+'/'+game_save_path+'/'+SaveName+'.pkl') == True:
            print("Save exist.")
            owq = input("Overwrite: (y/n)")
            if owq == 'y':
                print("Overwriteing Save")
                with open(game_loc+'/'+game_save_path+'/'+SaveName+'.pkl', 'wb') as f:
                    pickle.dump(RealmSaveF, f)
            elif owq == 'n':
                print("Did not create save.")
    elif confirm == '2':
        return
    else:
        print("Unknown choice!\n")
        Realms()

def Settings():
    print(Style.RESET_ALL)
    print(Fore.YELLOW + "Settings")
    #print(Fore.CYAN + "1. ")
    print(Fore.RED + "0. Return")
    print(Style.RESET_ALL)
    choice = input(Style.BRIGHT + "Choose Setting: ")
    print(Style.RESET_ALL)
    if choice == '0':
        return
    elif choice == '1':
        pass
    else:
        Settings()

ctrl_c_count = 0
    
def game_sys_menu():
    print(Style.BRIGHT + "- - - - - - - - - - -")
    print(Style.RESET_ALL)
    print("1. Quit")
    print("2. Save")
    print("0. Return")
    choice = input(Style.BRIGHT + "Input: ")
    print(Style.RESET_ALL)
    if choice == '0':
        return
    elif choice == '1':
        Realms()
    elif choice == '2':
        pass
        

def game_loop(save_data_dict):
    global PLYR_data
    PLYR_data = save_data_dict['Player']
    print(Fore.MAGENTA + "\n\nWelcome to the Realms!")
    signal.signal(signal.SIGINT, handle_sigint_gml)
    while True:
        print(Style.RESET_ALL)
        print("- _ - _ - _ - _ - _ - _ - _ -")
        print(Fore.CYAN)
        print("1. ")
        print("2. Player")
        print("3. Move")
        print("0. Game sys Menu")
        print(Style.RESET_ALL)
        choice = input(Style.BRIGHT + "Choose: ")
        print(Style.RESET_ALL)
        if choice == '0':
            game_sys_menu()
        elif choice == '1':
            pass
        elif choice == '2':
            print(save_data_dict['Player'])
        elif choice == '3':
            game_movement()
        else:
            global ctrl_c_count
            ctrl_c_count = 0

def Player(updt_dict):
    if updt_dict is None:
        pass
    else:
        pass
        

def combat(Enemyi):
    print("! --- Combat --- !")
    print(f" Enemy: {Enemyi}")
    print("--- Commands ---")
    print('"run" Attempt to exit combat')
    print('"skills" Show and use skills')
    print(Style.RESET_ALL)
    while True:
        choice = input("ATCK: ")
        #print(f"\033[2A")
        if choice.lower() == 'run':
            ranRand = random.randint(1, 4)
            PLYR_data['Health'] -= random.randint(1, 5)
            print("Health: ",PLYR_data['Health'],"/",PLYR_data['Max_Health'])
            print(Style.RESET_ALL)
            if ranRand > 1:
                return
            else:
                print("Failed to escape!")
        if choice.lower() == 'skills':
            print(PLYR_data['Skills'])

Enemies = {
    "Common": {
        "Small Slime": {
            "Max_Health": 25,
            "Health": 25,
        },
        "Common Thug": {
            "Max_Health": 50,
            "Health": 50,
            "Skills": [
                SkillsDB['Basic Sword Attack'],
                SkillsDB['Basic fast run'],
            ]
        },
    },
    "Uncommon": {
        "Big Slime": {
            "Max_Health": 50,
            "Health": 50,
        },
    },
    "Rare": {
        
    },
}
HC = {
    "Nothing": "",
    "Enemy": Enemies,
}

mv_left = True
mv_right = True

def game_movement():
    global mv_left
    global mv_right
    #print(Fore.GREEN + Style.BRIGHT + '"2" "DOWN"', Style.RESET_ALL + "Move Backward")
    print(Fore.GREEN + Style.BRIGHT + '"1" "UP"', Style.RESET_ALL + "Move Forward")
    if mv_left == True:
        print(Fore.GREEN + Style.BRIGHT + '"2" "LEFT"', Style.RESET_ALL + "Move Left")
    elif mv_left == False:
        print(Fore.GREEN + Style.DIM + '"2" "LEFT"', Style.RESET_ALL + Style.DIM + "Move Left")
    if mv_right == True:
        print(Fore.GREEN + Style.BRIGHT + '"3" "RIGHT"', Style.RESET_ALL + "Move Right")
    elif mv_right == False:
        print(Fore.GREEN + Style.DIM + '"3" "RIGHT"', Style.RESET_ALL + Style.DIM + "Move Right")
    print(Fore.LIGHTYELLOW_EX + "\n 0. Return")
    print(Style.RESET_ALL)
    chocie = input("Move: ")
    if chocie == '0':
        return
    elif chocie == 'UP' or chocie == '1':
        mv_left = True
        mv_right = True
        chanc()
        game_movement()
    elif (chocie == 'LEFT' or chocie == '2') and mv_left == True:
        mv_right = False
        chanc()
        game_movement()
    elif (chocie == 'RIGHT' or chocie == '3') and mv_right == True:
        mv_left = False
        chanc()
        game_movement()
    else:
        game_movement()
        #return
def chanc():
    rand = random.randint(1, len(HC))-1
    rand_enemy = random.randint(1, len(Enemies["Common"]))-1
    #print(rand)
    li = list(HC.keys())[rand]
    enemy = Enemies["Common"].get(list(Enemies['Common'].keys())[rand_enemy])#HC.get(list(Enemies.keys())[rand_enemy])
    print("--- CHANCE ---")
    if li == 'Enemy':
        print(f"{li}: {list(Enemies['Common'].keys())[rand_enemy]}")
    else:
        print(li)
    print("--- END ---")
    print(Style.RESET_ALL)
    if li == 'Enemy':
        combat(enemy)

def handle_sigint_gml(sig, frame):
    global ctrl_c_count
    ctrl_c_count += 1
    if ctrl_c_count >= 2:
        print(Style.RESET_ALL)
        print("\nExiting...")
        sys.exit(0)
    print("\nPress Ctrl+C again to exit.")

if __name__ == '__main__':
    main()