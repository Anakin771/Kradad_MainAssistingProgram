"""
***********************************************

Author: MontyGUI

Description
This script includes every functions that revolves
around boss's stats, such as generating a single boss stats,
generating group boss, etc.

***********************************************
"""
import math
import random


def round_half_up(n, decimals=0):
    mtp = 10 ** decimals
    return math.floor(n * mtp + 0.5) / mtp


def round_basic(n, decimals=0):
    rounded_abs = round_half_up(abs(n), decimals)
    return math.copysign(rounded_abs, n)


def random_boss_stat(boss_lv, player_num, show_stat=True):
    # Boss' LV = All Player's average LV
    boss_hp = boss_lv * player_num * 1000
    boss_stat_pt = boss_lv if boss_lv >= 10 else boss_lv * 5
    boss_stat_mtp = 100 if boss_lv >= 10 else 20

    boss_patk = 0
    boss_matk = 0
    boss_pdef = 0
    boss_mdef = 0

    count = 0

    while count < boss_stat_pt:
        boss_rand = random.randint(1, 4)

        if boss_rand == 1:
            boss_patk += 1 * boss_stat_mtp
        elif boss_rand == 2:
            boss_matk += 1 * boss_stat_mtp
        elif boss_rand == 3:
            boss_pdef += 1 * boss_stat_mtp
        elif boss_rand == 4:
            boss_mdef += 1 * boss_stat_mtp

        count += 1

    if show_stat:
        print("---------------------------------")
        print("BOSS STATS:")
        print(f"HP: {boss_hp}")
        print(f"P. ATK: {boss_patk}")
        print(f"M. ATK: {boss_matk}")
        print(f"P. DEF: {int(boss_pdef / 2)}")
        print(f"M. DEF: {int(boss_mdef / 2)}")
        print("---------------------------------")

    return {
        "HP": boss_hp,
        "PATK": boss_patk,
        "MATK": boss_matk,
        "PDEF": boss_pdef,
        "MDEF": boss_mdef
    }


def random_boss_stat_multi(boss_lv, player_num, qty, show_stat=True):
    # Boss' LV = All Player's average LV
    boss_hp = int((boss_lv * player_num * 1000) / 3)
    boss_list = []
    count = 0
    reduce_mtp = 0.8

    while count < qty:
        single_boss_stat = random_boss_stat(boss_lv, player_num, show_stat=False)
        current_boss = {
            "HP": boss_hp,
            "PATK": int(round_basic(single_boss_stat["PATK"] * reduce_mtp, -1)),
            "MATK": int(round_basic(single_boss_stat["MATK"] * reduce_mtp, -1)),
            "PDEF": int(round_basic(single_boss_stat["PDEF"] * reduce_mtp, -1)),
            "MDEF": int(round_basic(single_boss_stat["MDEF"] * reduce_mtp, -1))
        }

        boss_list.append(current_boss)
        count += 1

    if show_stat:
        boss_count = 1

        print("**********************************************")
        for boss in boss_list:
            print(f"Boss #{boss_count} Stats:")
            for stat, value in boss.items():
                if stat == "PDEF" or stat == "MDEF":
                    print(f"{stat}: {int(value / 2)}")
                else:
                    print(f"{stat}: {value}")

            print("\n---------------------------------------------\n")
            boss_count += 1
        print("**********************************************")

    return boss_list
