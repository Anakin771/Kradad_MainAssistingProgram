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


STARTING_BASE_ROLL = 40
STARTING_MTP = 5

BONUS_BASE_ROLL = 20
BONUS_MTP = 5

EARLY_REQ_XP_RATE = 1.5
MID_REQ_XP_RATE = 1.65
LATE_REQ_XP_RATE = 1.8

ITEM_DECLINED_BONUS_MTP = 1.2

FALLEN_ALLY_PENALTY = 0.1


def random_char_stat_single(base_roll_point, multiplier, header_text=None, show_stat=True):
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
        print(f" HP: {hp} pts.")
        print(f" P. ATK: {p_atk} pts.")
        print(f" M. ATK: {m_atk} pts.")
        print(f" P. DEF: {p_def} pts.")
        print(f" M. DEF: {m_def} pts.")
        print(f" FREE: {free_stat} pts.")
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
        STARTING_BASE_ROLL,
        STARTING_MTP,
        header_text="------------ Step 1: Randomizing Starting Stats ------------"
    )
    if starting is None:
        return None

    bonus = random_char_stat_full(
        BONUS_BASE_ROLL,
        BONUS_MTP,
        header_text="------------ Step 2: Randomizing Bonus Rate ------------"
    )
    if bonus is None:
        return None

    clear()
    print("***********************\n"
          "       YOUR STATS:     \n"
          "***********************\n")

    print(" Starting Stat Points:")
    for stat, pts in starting.items():
        print(f" {stat}: {pts} pts.")
    print("----------------------")
    print(" Bonus Rate Points:")
    for stat, pts in bonus.items():
        print(f" {stat}: {pts} pts.")

    return {
        "starting": starting,
        "bonus": bonus
    }


def calculate_level_up(char_lv, current_xp, gained_xp, fallen=0, item_accepted=True, show_stat=True):
    new_char_lv = char_lv
    req_xp = cal_req_xp(new_char_lv)

    # Reduce gained XP due to fallen party member
    fallen_penalty_rate = 1 - (fallen * FALLEN_ALLY_PENALTY)
    gained_xp = max(gained_xp * fallen_penalty_rate, 0)

    # +20% XP bonus for players who declined dropped item
    gained_xp *= ITEM_DECLINED_BONUS_MTP if not item_accepted else 1

    # For LV 10 and lower, XP Gained is x2
    gained_xp *= 2 if char_lv <= 10 else 1

    # Calculate Level Up
    total_xp = current_xp + int(rounder.round_basic(gained_xp))
    gained_sp = 0
    while total_xp >= req_xp:
        new_char_lv += 1
        total_xp -= req_xp
        req_xp = cal_req_xp(new_char_lv)

        if new_char_lv % 10 == 0:
            gained_sp += 2
        elif new_char_lv % 5 == 0:
            gained_sp += 1

    notice = ""
    if new_char_lv <= char_lv:
        if gained_xp <= 0 < fallen:
            notice = "Too many players have fallen."
        else:
            notice = "Your total XP does not reach target XP."

    if show_stat:
        extra_cal = False

        if char_lv <= 10:
            print(" (Player with LV 10 or lower gets x2 XP)")
            extra_cal = True

        if fallen > 0:
            print(f" ({fallen} Party member(s) have fallen, -{min(int(fallen * 10), 100)}% XP Penalty)")
            extra_cal = True

        if not item_accepted:
            print(f" (Item Declined: +{int(rounder.round_basic((ITEM_DECLINED_BONUS_MTP - 1) * 100))}% XP)")
            extra_cal = True

        if gained_xp <= 0 < fallen:
            print(
                "--------------------------------\n"
                " Too many players have fallen!\n"
                " You do not gain any XP...\n"
                "--------------------------------\n"
            )
        elif new_char_lv > char_lv:
            print("---------------------------------")
            print(" You have leveled up!")
            print(f" Your Character's LV: {char_lv} -> {new_char_lv}")
            print(f" Remainder XP: {current_xp} -> {total_xp}")
            print(f" To next LV: {req_xp} XP")
            if gained_sp > 0:
                print(f" You have received {gained_sp} Skill Point(s).")
            print("---------------------------------")
        else:
            print("---------------------------------")
            print(" Sorry, but you did not level up...")
            print(f" Your Current XP: {current_xp} -> {total_xp}")
            print("---------------------------------")

        if extra_cal:
            print(" * Bonus Calculation goes from top to bottom.")

    return {
        "lv_up": bool(new_char_lv > char_lv),
        "item_decl": bool(not item_accepted),
        "fallen": fallen,
        "fallen_penalty": min(int(fallen * 10), 100),
        "old": {
            "lv": char_lv,
            "rem_xp": current_xp
        },
        "new": {
            "lv": new_char_lv,
            "rem_xp": total_xp
        },
        "gained_xp": gained_xp,
        "gained_sp": gained_sp,
        "note": notice
    }


def cal_req_xp(char_lv):
    if char_lv <= 30:
        return int(rounder.round_basic(100 * (char_lv ** EARLY_REQ_XP_RATE), -2))
    elif char_lv <= 60:
        return int(rounder.round_basic(100 * (char_lv ** MID_REQ_XP_RATE), -2))
    else:
        return int(rounder.round_basic(100 * (char_lv ** LATE_REQ_XP_RATE), -2))
