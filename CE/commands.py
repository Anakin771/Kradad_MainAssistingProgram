"""
***********************************************

Author: MontyGUI

Description
This script extends main.py,
it includes the functionality of the main scripts
used in console edition of the app.

***********************************************
"""
import bossStat
import itemStat
import playerStat

from os import system, name
# import GUI.mainFrame as Gui

ITEM_TYPE_MAPPING = {
    "weapon": "wpn",
    "armor": "amr",
    "accessories": "acc",
    "wpn": "wpn",
    "amr": "amr",
    "acc": "acc"
}

DROPPED_ITEM_CHOICE_MAPPING = {
    "accepted": True,
    "ac": True,
    "declined": False,
    "dc": False,
    "none": True
}

COMMAND_LIST = {}


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


def get_int_input(query_txt="Please enter an integer: ", non_zero=False, non_neg=False, no_cancel=False):
    """
    Gather integer input listed in the dictionary, with query texts included
    :param query_txt: Optional - The text which query the user
    :param non_zero: Optional - specify if the integer must be non-zero
    :param non_neg: Optional - specify if the integer must be non-negative
    :param no_cancel: Optional - specify if the user cannot cancel out from the input
    :return: Returns an integer which the user has given, None boolean if the user cancels.
    """
    while True:
        in_txt = input(query_txt)
        try:
            int_val = int(in_txt)
            if non_zero and int_val == 0:
                print("You must enter a non-zero integer!")
                if not no_cancel:
                    print("(or you can cancel this command by typing 'cancel')")
                print()
                continue
            elif non_neg and int_val < 0:
                print("You must enter a non-negative integer!")
                if not no_cancel:
                    print("(or you can cancel this command by typing 'cancel')")
                print()
                continue
            print()
            return int_val
        except ValueError:
            if in_txt.lower() == "cancel" and not no_cancel:
                print("\n-- Action Canceled --")
                return None
            print("Sorry, you must enter an integer here!")
            if not no_cancel:
                print("(or you can cancel this command by typing 'cancel')")
            print()


def get_choice_input(choices, query_text="Please pick one from these options", no_cancel=False, ignore_case=True):
    """
    Get user input that is listed within one of the choices
    :param choices: list of choices to be picked by user.
    :param query_text: Text for asking the user, default is "Please pick one from these options", it is appended by
    choices and ended with a colon (:)
    :param no_cancel: Specify if the user cannot cancel action, default is False.
    :param ignore_case: Specify if the options ignore letter-casing, default is True.
    :return: A string of the choice selected, None if the user cancels.
    """
    full_query_text = f"{query_text} - {choices}: "
    if ignore_case:
        for idx in range(len(choices)):
            choices[idx] = choices[idx].lower()

    while True:
        in_txt = input(full_query_text)
        if ignore_case:
            in_txt = in_txt.lower()
        if in_txt == "" and not no_cancel:
            print("\n-- Action Canceled --")
            return None
        if in_txt in choices:
            print()
            return in_txt
        else:
            print("You must pick from one of the options!")
            if not no_cancel:
                print("(You can cancel this by not typing anything and press Enter.)")
            print()
            continue


def generate_boss():
    """
    Generate a boss, or multiple bosses
    :return: None if the user cancels the action.
    """
    avg_lv = get_int_input("Step 1 - Please enter your party's average LV: ", non_zero=True, non_neg=True)
    if avg_lv is None:
        return None
    p_num = get_int_input("Step 2 - Please enter the number of members in your party: ", non_zero=True, non_neg=True)
    if p_num is None:
        return None
    boss_qty = get_int_input("Step 3 - Please enter the number of bosses: ", non_zero=True, non_neg=True)
    if boss_qty is None:
        return None

    difficulty = get_choice_input(["Noob", "Easy", "Normal", "Hard", "Hardcore"],
                                  "Step 4 - Please select the difficulty")
    if difficulty is None:
        return None

    if boss_qty == 1:
        bossStat.random_boss_stat(avg_lv, p_num, diff=difficulty)
    else:
        bossStat.random_boss_stat_multi(avg_lv, p_num, boss_qty, diff=difficulty)


def generate_boss_item():
    """
    Generate an item dropped from bosses
    :return: None if the user cancels the action.
    """
    boss_lv = get_int_input("Step 1 - Please enter boss' LV: ", non_zero=True, non_neg=True)
    if boss_lv is None:
        return None

    item_type_in = get_choice_input(
        ["Weapon", "wpn", "Armor", "amr", "Accessories", "acc"],
        "Step 2 - Please enter boss' item type"
    )
    if item_type_in is None:
        return None

    item_type = ITEM_TYPE_MAPPING.get(item_type_in)

    itemStat.random_item_stat(boss_lv, item_type=item_type)


def calculate_char_lv():
    """
    Calculate character's level progression (LV up)
    :return: None if the user cancels the action.
    """
    char_lv = get_int_input("Step 1 - Please enter your character's current LV: ", non_zero=True, non_neg=True)
    if char_lv is None:
        return

    rem_xp = get_int_input("Step 2 - Please enter your character's remainder XP: ", non_neg=True)
    if rem_xp is None:
        return

    gained_xp = get_int_input("Step 3 - Please enter gained XP: ", non_zero=True, non_neg=True)
    if gained_xp is None:
        return

    fallen_party_mem = get_int_input("Step 4 - Please enter the number of fallen party member: ", non_neg=True)
    if fallen_party_mem is None:
        return

    item_choice = get_choice_input(
        ["Accept", "ac", "Decline", "dc", "None"],
        "Step 5 - Did you accept any Boss Item? (Pick 'None' when the Boss drops no Item)\n"
    )
    if item_choice is None:
        return
    else:
        choice_bool = DROPPED_ITEM_CHOICE_MAPPING.get(item_choice, False)

    playerStat.calculate_level_up(char_lv, rem_xp, gained_xp, fallen=fallen_party_mem, item_accepted=choice_bool)


def craft_item():
    """
    Begin crafting items based on the user's material and LV.
    :return: None if the user cancels the action.
    """
    item_type_choices = ["Weapon", "wpn", "Armor", "amr", "Accessories", "acc"]

    player_lv = get_int_input("Step 1 - Please enter your character's LV: ", non_zero=True, non_neg=True)
    if player_lv is None:
        return None

    # Get material type for Material A
    mat_a = get_choice_input(
        item_type_choices,
        "Step 2 - Please enter the type of the FIRST material"
    )
    if mat_a is None:
        return None

    # Get material type for Material B
    mat_b = get_choice_input(
        item_type_choices,
        "Step 3 - Please enter the type of the SECOND material"
    )
    if mat_b is None:
        return None

    # Get material type for Material C
    mat_c = get_choice_input(
        item_type_choices,
        "Step 4 - Please enter the type of the THIRD material"
    )
    if mat_c is None:
        return None

    mat_a = ITEM_TYPE_MAPPING.get(mat_a, None)
    mat_b = ITEM_TYPE_MAPPING.get(mat_b, None)
    mat_c = ITEM_TYPE_MAPPING.get(mat_c, None)

    itemStat.craft_item(mat_a, mat_b, mat_c, player_lv)


def cmd_help():
    """
    List all possible commands.
    """
    print("List of all possible commands:")
    for cmd, info in HELP_LIST.items():
        print(f"{cmd}\t{info}")
    print("quit / exit / stop\tQuit the Program.")


COMMAND_LIST.update({
    "new_char": lambda: playerStat.random_starting_char(),
    "boss": lambda: generate_boss(),
    "boss_item": lambda: generate_boss_item(),
    "level_up": lambda: calculate_char_lv(),
    "craft_item": lambda: craft_item(),
    "help": lambda: cmd_help(),
})

HELP_LIST = {
    "new_char": "Start new character - Starting Stat Points and Bonus Rate Points is randomized\n",
    "boss": generate_boss.__doc__.strip("\n").partition(":return:")[0],
    "boss_item": generate_boss_item.__doc__.strip("\n").partition(":return:")[0],
    "level_up": calculate_char_lv.__doc__.strip("\n").partition(":return:")[0],
    "craft_item": craft_item.__doc__.strip("\n").partition(":return:")[0],
    "help": cmd_help.__doc__.strip("\n").partition(":return:")[0],
}
