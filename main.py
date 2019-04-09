#!/usr/bin/python
"""Program for setting up and removing trainer."""

import os
import shutil
import time
import textwrap
import json
import ctypes


from libs import terminal_text_effect


def set_preferences():
    # root_path = os.getcwd()
    drag_menu = """Drag file here or manually type out the path,
    """
    print("")
    pref_file = raw_input("""Drag file here or manually type out the path,\n
        Press \'\033[1;32;40m;Enter {RESET}\' to continue...\n
        \n::""").replace("{RESET}", "RESET")
    clear()
    if not pref_file:
        return
    response = raw_input("""Is this the correct path?\n
    {}\n[ y ] or [ n ]: """)
    if response == "y":
        clear()
        print("this")
    elif response == "n":
        clear()
        set_preferences()
    else:
        return
    # filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
    # json_args = json.dumps(pref_file)
    #
    # if filename:
    #     with open(filename, 'r') as file:
    #         json_args = json.load(file)
    #         file.close()
    # for key in json_args.keys():
    #     if key == "$$DIRECTORY":
    #         print("{}".format(key.value()))
    # file.close()
    # return


def read_pref():
    root_path = os.getcwd()
    print("Here we go.")
    pref_file = ""
    pref_folder = ""
    if os.name == "nt":
    #     pref_folder = PureWindowsPath(root_path+"\\preferences")
    #     pref_file = str(pref_folder) + "\\wrkdirs.json"
    # else:
    #     pref_folder = Path(pref_folder)
    #     pref_file = Path(pref_file)

    # print("\033[1;32;40m" + "Found!" + "\033[1;36;40m" + "{: >100}".format(str(pref_folder)))
        print("")

    pref_file = str(pref_folder) + "\\wrkdirs.json"
    # json_args = json.dumps(pref_file)
    # with open(pref_file, 'r') as file:
    #     json_args = json.load(file)
    #     print(json.dumps(json_args, indent=4, sort_keys=True))
    # file.close()
    return pref_file


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


def _menu_print(root_dir):
    pref_dir = root_dir + "\\preferences"
    os.chdir(pref_dir)
    print(pref_dir)
    json_file = pref_dir + "\\wrkdirs.json"
    print(json_file)
    with open(json_file, 'r') as file:
        json_data = json.dumps(file, indent=4)
    print(json_data)
    for line in json_data:
        print(line)
    file.close()
    total_options = 4
    print("STOP!")
    clear()
    print("\n\n\n{:=^60}".format("  WARNING!  "))
    print("")
    _ = raw_input()
    print("{:-^60}".format("MENU"))
    print("{: ^60}".format(""))
    mods = terminal_text_effect(text="Install Trainer V", color='red')
    print("1. {}".format(mods))
    print("2. Uninstall Trainer V")
    print("3. Open GTA V folder")
    print("{: ^60}".format(""))
    print("{:-^60}".format(""))
    print("{: ^60}".format(""))
    print("4. Exit")
    print("{:-^60}".format(""))
    return (int(total_options))


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
    root_dir = os.getcwd()
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    loop = True

    while loop:
        print(root_dir)
        _ = raw_input()
        try:
            clear()
            items = _menu_print(root_dir)
            user = _menu_select()

            # if user == 1:
            #     clear()
            #     print("{:-^60}".format("MOVE selected"))
            #     print("{: ^60}".format(""))
            #     try:
            #         _ = _move_in(TRAINER_DIR, GTA_DIR)
            #         print("{: ^60}".format(""))
            #         print("{:-^60}".format(""))
            #         print("{: ^60}".format(""))
            #         _ = raw_input("Success! Press enter.")
            #     except Exception as err:
            #         print("Ran into an issue when selecting: [{}], error: {}".format(user, err))
            #         _ = raw_input("Press \'Enter\' to continue...")
            # elif user == 2:
            #     clear()
            #     print("{:-^60}".format("REMOVE selected"))
            #     try:
            #         _move_out(TRAINER_DIR, GTA_DIR)
            #         print("{:-^60}".format(""))
            #         print("{: ^60}".format(""))
            #         _ = raw_input("Success! Press enter.")
            #     except Exception as err:
            #         print("Ran into an issue when selecting: {}, error: {}".format(user, err))
            #         raw_input("")
            # elif user == 3:
            #     path = os.path.realpath(GTA_DIR)
            #     os.startfile(path)
            #     raw_input("Opening dir now. Press anything to continue...")
            # elif user == 4:
            #     clear()
            #     raw_input("Exit has been selected. Press anything to continue...")
            #     clear()
            #     loop = False
            # else:
            #     _ = raw_input("Wrong option selection. Enter any key to try again...")
        except:
            _ = raw_input("Invalid input. Enter any key to try again...")
    return

if __name__ == "__main__":
    main()
