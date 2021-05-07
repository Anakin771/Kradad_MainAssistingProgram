"""
***********************************************

Author: MontyGUI
Last Edit: 24/4/2021

Copyright 2021 - MontyGUI
(This copyright is extended to all files within this project
aside Python's built-in files and third-party open-sources)

***********************************************
"""
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from CE.commands import *
import time

VERSION = "1.5.0b"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    header_bar = "********************************************************"
    version_text = f"Version: {VERSION}".center(len(header_bar))
    clear()
    print(
        "\n"
        f" {header_bar}\n"
        " Game Kradad - Game Assisting Program (CONSOLE EDITION)\n"
        f" {version_text}\n"
        f" {header_bar}\n"
    )
    while True:
        cmd_input = input(" Please enter your command: ")

        print()

        if cmd_input.lower() in ["exit", "quit", "stop"]:
            print(" ----** See you soon! **----")
            time.sleep(1.0)
            break

        get_cmd = COMMAND_LIST.get(cmd_input.lower(), lambda: print(" There are no such commands."))
        get_cmd()
        print("\n----------------********----------------\n")
    # Gui.run_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
