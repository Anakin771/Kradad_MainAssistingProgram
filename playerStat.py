"""
***********************************************

Author: MontyGUI

Description
This script includes every functions that revolves
around player's stats, including initial stats generation,
calculate levels, etc.

***********************************************
"""

import rounder
import random
from os import system, name


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


DEFAULT_STARTING_BASE_ROLL = 40
DEFAULT_STARTING_MTP = 5

DEFAULT_BONUS_BASE_ROLL = 20
DEFAULT_BONUS_MTP = 5


def random_char_stat_single(base_roll_point, multiplier, header_text="", show_stat=True):
    """
    Randomize a character stat points only once upon given factors.
    :param base_roll_point: The number of times to random a category of stats
    :param multiplier: The number which is multiplied after one roll point is assigned to a category
    :param header_text: Optional - The text that will be written in the console as a header.
    :param show_stat: Optional - Triggers displaying the randomized stat points if set to True
    :return: Returns a dictionary of a randomized character stat points
    """
    if header_text is not None:
        print(header_text)

    count = 0

    hp = 0
    p_atk = 0
    m_atk = 0
    p_def = 0
    m_def = 0
    free_stat = 0

    while count < base_roll_point:
        stat_cat = random.randint(1, 6)

        if stat_cat == 1:
            hp += 1 * multiplier
        elif stat_cat == 2:
            p_atk += 1 * multiplier
        elif stat_cat == 3:
            m_atk += 1 * multiplier
        elif stat_cat == 4:
            p_def += 1 * multiplier
        elif stat_cat == 5:
            m_def += 1 * multiplier
        elif stat_cat == 6:
            free_stat += 1 * multiplier

        count += 1

    if show_stat:
        print("-----------------------------")
        print(f"HP: {hp} pts.")
        print(f"P. ATK: {p_atk} pts.")
        print(f"M. ATK: {m_atk} pts.")
        print(f"P. DEF: {p_def} pts.")
        print(f"M. DEF: {m_def} pts.")
        print(f"FREE: {free_stat} pts.")
        print("-----------------------------")

    return {
        'HP': hp,
        'PATK': p_atk,
        'MATK': m_atk,
        'PDEF': p_def,
        'MDEF': m_def,
        'FREE': free_stat
    }


def random_char_stat_full(base_roll_point, multiplier, header_text=""):
    """
    Randomize a character stat points upon given factors. (CONSOLE EDITION)
    :param base_roll_point: The number of times to random a category of stats
    :param multiplier: The number which is multiplied after one roll point is assigned to a category
    :param header_text: Optional - The text that will be written in the console as a header.
    :return: Returns a dictionary of a randomized character stat points that has been chosen by the user;
    None if the user cancels.
    """
    while True:

        sample_stat_points = random_char_stat_single(
            base_roll_point,
            multiplier,
            header_text=header_text,
            show_stat=True
        )

        try:
            confirm = str(input("Choose these stats? (Y/N/Cancel): ")).lower()
            if confirm == 'y':
                return sample_stat_points
            elif confirm == 'cancel':
                print("Action Canceled")
                return None
            else:
                clear()
                continue
        except TypeError:
            print("An error has occurred, try again.")


def random_starting_char():
    """
    Begin randomizing new character's Stat Points
    :return: Dictionary of Starting Stats and Bonus Rate;
    None if the action is canceled.
    """
    starting = random_char_stat_full(
        DEFAULT_STARTING_BASE_ROLL,
        DEFAULT_STARTING_MTP,
        header_text="------------ Step 1: Randomizing Starting Stats ------------"
    )
    if starting is None:
        return None

    bonus = random_char_stat_full(
        DEFAULT_BONUS_BASE_ROLL,
        DEFAULT_BONUS_MTP,
        header_text="------------ Step 2: Randomizing Bonus Rate ------------"
    )
    if bonus is None:
        return None

    clear()
    print("***********************\n"
          "       YOUR STATS:     \n"
          "***********************\n")

    print("Starting Stat Points:")
    for stat, pts in starting.items():
        print(f"{stat}: {pts} pts.")
    print("----------------------")
    print("Bonus Rate Points:")
    for stat, pts in bonus.items():
        print(f"{stat}: {pts} pts.")

    return {
        "starting": starting,
        "bonus": bonus
    }


def calculate_level_up(char_lv, current_xp, gained_xp):
    new_char_lv = char_lv
    req_xp = cal_req_xp(new_char_lv)

    # For LV 9 and lower, XP Gained is x2
    gained_xp *= 2 if char_lv < 10 else 1

    total_xp = current_xp + gained_xp
    while total_xp >= req_xp:
        new_char_lv += 1
        total_xp -= req_xp
        req_xp = cal_req_xp(new_char_lv)

    if new_char_lv > char_lv:
        print("---------------------------------")
        print("You have leveled up!")
        print(f"Your Character's LV: {char_lv} -> {new_char_lv}")
        print(f"Remainder XP: {current_xp} -> {total_xp}")
        print(f"To next LV: {req_xp} XP")
        print("---------------------------------")
    else:
        print("---------------------------------")
        print("Sorry, but you did not level up...")
        print(f"Your Current XP: {current_xp} -> {total_xp}")
        print("---------------------------------")


def cal_req_xp(char_lv):
    if char_lv <= 30:
        return int(rounder.round_basic(100 * (char_lv ** 1.5), -2))
    elif char_lv <= 60:
        return int(rounder.round_basic(100 * (char_lv ** 1.65), -2))
    else:
        return int(rounder.round_basic(100 * (char_lv ** 1.8), -2))