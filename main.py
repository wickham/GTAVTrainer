#!/usr/bin/python
"""Program for setting up and removing trainer."""

import os, shutil, time, textwrap, json
from pathlib import Path, PureWindowsPath
from colorama import init as color_init
from colorama import Style

TRAINER_DIR = ''
GTA_DIR = ''


def read_pref():
    color_init()
    root_path = os.getcwd()
    print("Here we go.")
    if os.name == "nt":
        pref_folder = PureWindowsPath(root_path+"\\preferences")
    else:
        pref_folder = Path(pref_folder)

    print("\033[1;32;40m" + "Found!" + "\033[1;36;40m" + "{: >100}".format(str(pref_folder)))
    print(Style.RESET_ALL)

    json_args = json.dumps(_file)

## Text menu in Python
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def breaker():
    if os.name == 'nt':
        return "\\"
    else:
        return "/"


# def cmp_newest_file(sent_file, orig_file):
#     print("{}\n{}".format(sent_file, orig_file))
#     sent_mod_time = os.stat(sent_file).st_ctime
#     orig_mod_time = os.stat(orig_file).st_ctime
#     # now_time = time.time() - (30 * 60)
#     if sent_mod_time == orig_mod_time:
#         print("No changes needed.")
#         _ = raw_input("Press \'Enter\' to continue... ")
#         return True
#     else:
#         user = raw_input("{:^60}\n ORIGINAL -----> {}\|{:>60}\n REPLACEMET ----> {}\|{:>60}\n\nPRESS [y] or [n]: ".format("WARNING: OVERWRITE OCCURRING :",orig_mod_time, orig_file, sent_mod_time, sent_file))
#         if user == "y":
#             return sent_file
#         else:
#             return orig_file


def _menu_print():
    total_options = 4
    print("{:-^60}".format("MENU"))
    print("{: ^60}".format(""))
    print("1. Install Trainer V")
    print("2. Uninstall Trainer V")
    print("3. Open GTA V folder")
    print("{: ^60}".format(""))
    print("{:-^60}".format(""))
    print("{: ^60}".format(""))
    print("4. Exit")
    print("{:-^60}".format(""))
    return total_options


def _menu_select(num_menu_inputs):
    choice = raw_input("Enter your choice [1-{}]: ".format(num_menu_inputs))
    return (int(choice))


def _move_in(TRAINER_DIR, GTA_DIR):
    if not os.listdir(TRAINER_DIR):
        print("No files were found in Trainer Dir.")
        _ = raw_input("Press Enter to continue...")
    for name in os.listdir(TRAINER_DIR):
        if name.startswith("TrainerV") or name.startswith("ScriptHookV") or name.startswith("dinput8") or name.startswith("trainerv"):
            orig = TRAINER_DIR + breaker() + name
            dest = GTA_DIR + breaker() + name
            # if cmp_newest_file(orig, dest):
            #     return
            # else:
            #     orig = cmp_newest_file(orig, dest)
            print("{:=^60}".format(" MOVING "))
            shutil.copyfile(orig, dest)
            print("MOVED: {}".format(name))
        else:
            print("Found invalid file! : {}".format(name))


def _move_out(TRAINER_DIR, GTA_DIR):
    all_files = []
    for name in os.listdir(GTA_DIR):
        if name.startswith("TrainerV") or name.startswith("ScriptHookV") or name.startswith("dinput8") or name.startswith("trainerv"):
            dest = TRAINER_DIR + breaker() + name
            orig = GTA_DIR + breaker() + name
            shutil.move(orig, dest)
            print("DELETED: {}".format(name))
        else:
            all_files.append(name)
    if all_files:
        all_files = ",".join(all_files)
        print("{:-^60}".format(""))
        print("{: ^60}".format(""))
        print("Skipped file(s) :\n")
        wrapper = textwrap.TextWrapper(width=60)
        print(wrapper.fill(text=all_files))


def main():
    os.chdir(GTA_DIR)
    loop = True

    while loop:
        try:
            clear()
            items = _menu_print()
            user = _menu_select(items)

            if user == 1:
                clear()
                print("{:-^60}".format("MOVE selected"))
                print("{: ^60}".format(""))
                try:
                    _ = _move_in(TRAINER_DIR, GTA_DIR)
                    print("{: ^60}".format(""))
                    print("{:-^60}".format(""))
                    print("{: ^60}".format(""))
                    _ = raw_input("Success! Press enter.")
                except Exception as err:
                    print("Ran into an issue when selecting: [{}], error: {}".format(user, err))
                    _ = raw_input("Press \'Enter\' to continue...")
            elif user == 2:
                clear()
                print("{:-^60}".format("REMOVE selected"))
                try:
                    _move_out(TRAINER_DIR, GTA_DIR)
                    print("{:-^60}".format(""))
                    print("{: ^60}".format(""))
                    _ = raw_input("Success! Press enter.")
                except Exception as err:
                    print("Ran into an issue when selecting: {}, error: {}".format(user, err))
                    raw_input("")
            elif user == 3:
                path = os.path.realpath(GTA_DIR)
                os.startfile(path)
                raw_input("Opening dir now. Press anything to continue...")
            elif user == 4:
                clear()
                raw_input("Exit has been selected. Press anything to continue...")
                clear()
                loop = False
            else:
                _ = raw_input("Wrong option selection. Enter any key to try again...")
        except:
            _ = raw_input("Invalid input. Enter any key to try again...")
    return

if __name__ == "__main__":
    main()
