
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

def main():
    print(Style.RESET_ALL)
    print('\n------------')
    print("Welcome! \n")
    try:
        while True:
            print("- - - - - -")
            print("REALMS")
            print("1. Realms")
            print("2. Settings")
            print("0. Quit")
            print('')
            choice = input(Style.BRIGHT + "Path: ")
            print(Style.RESET_ALL)
            if choice == '0':
                break
            elif choice == '1':
                Realms()
            elif choice == '2':
                Settings()
            elif choice == "000":
                test_func()
    except KeyboardInterrupt:
        print(Style.RESET_ALL)

def Realms():
    print("1. Load Realm")
    print("2. Create Realm")
    print("3. View Realms Data")
    print("0. Return")
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
    print(f"Savefolder: {os.path.abspath(game_save_path)}")
        
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
        pass
    print("\n1. Load world by name")
    #print("2. Load world by ID ") #Under work #Does not work for now
    print("0. Return")
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
    SaveName = input("Enter Realm Name (savename): ")
    
    RealmSaveF = {
        "Name": SaveName,
        "Player": {
            "Health": 100,
            "Max_Health": 100,
        },
    }
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
    elif confirm == '2':
        return
    else:
        print("Unknown choice!\n")
        Realms()

def Settings():
    print('')
    print("Settings")
    print("1. ")
    print("0. Return")
    print('')
    choice = input(Style.BRIGHT + "Choose Setting: ")
    print(Style.RESET_ALL)
    if choice == '0':
        return
    elif choice == '1':
        pass

ctrl_c_count = 0
    
def game_sys_menu():
    print(Style.BRIGHT + "- - - - - - - - - - -")
    print(Style.RESET_ALL)
    print("0. Return")
    choice = input(Style.BRIGHT + "Input: ")
    print(Style.RESET_ALL)
    if choice == '0':
        return
    
def test_func():
    dicter = {
        "Name": "SaveName",
        "Player": {
            "Health": 100,
            "Max_Health": 100,
        },
    }
    print(dicter['Player'])

def game_loop(save_data_dict):
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
            combat()
        elif choice == '2':
            print(save_data_dict)
        elif choice == '3':
            game_movement()
        else:
            global ctrl_c_count
            ctrl_c_count = 0


def combat():
    while True:
        choice = input("ATCK: ")
        print(f"\033[2A")
        if choice == '1':
            print("\nT")


Enemies = {
    "Common Thug": {
        "Max_Health": 50,
        "Health": 50
    },
}
HC = {
    "Nothing": "",
    "Enemy": Enemies['Common Thug']
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
    rand_enemy = random.randint(1, len(Enemies))-1
    #print(rand)
    li = list(HC.keys())[rand]
    enemy = HC.get(list(Enemies.keys())[rand_enemy])
    print("--- CHANCE ---")
    print(f"{li}: {enemy}")
    print("--- END ---")
    print(Style.RESET_ALL)

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