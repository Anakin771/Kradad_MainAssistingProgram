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


# Boss HP-by-LV Multiplier
EARLY_BOSS_HP_MTP = 700
MID_BOSS_HP_MTP = 850
LATE_BOSS_HP_MTP = 1000

# Multi-Boss-Fight Stats-Down Multiplier
MULTIPLE_BOSS_MTP = 0.8

# Rewards Multiplier
XP_MULTIPLIER = 1300
MONEY_MULTIPLIER = 100

# Difficulty names-to-rate tables...
DIFF_TO_LV_MAPPING = {
    "noob": -5,
    "easy": -3,
    "normal": 0,
    "hard": 3,
    "hardcore": 6
}
DIFF_TO_COIN_MAPPING = {
    "noob": -5,
    "easy": -1,
    "normal": 0,
    "hard": 3,
    "hardcore": 6
}
DIFF_TO_HP_MAPPING = {
    "noob": -2,
    "easy": -1,
    "normal": 0,
    "hard": 3,
    "hardcore": 8
}
DIFF_TO_ITEM_MAPPING = {
    "noob": "0",
    "easy": "1",
    "normal": "1 or 2",
    "hard": "2",
    "hardcore": "3"
}


def round_half_up(n, decimals=0):
    mtp = 10 ** decimals
    return math.floor(n * mtp + 0.5) / mtp


def round_basic(n, decimals=0):
    rounded_abs = round_half_up(abs(n), decimals)
    return math.copysign(rounded_abs, n)


def random_boss_stat(party_avg_lv, player_num, diff=None, show_stat=True):

    input_diff = True

    # Default value for diff if unspecified
    if diff is None:
        input_diff = False
        diff = "normal"

    # Get Boss LV Difficulty Rate
    lv_diff_rate = DIFF_TO_LV_MAPPING.get(diff, 0)

    # Get Boss HP Difficulty Rate
    hp_diff_rate = DIFF_TO_HP_MAPPING.get(diff, 0)

    # Get Boss Coin Reward Difficulty Rate
    money_diff_rate = DIFF_TO_COIN_MAPPING.get(diff, 0)

    # Get Boss Item Reward Difficulty Rate
    item_reward = DIFF_TO_ITEM_MAPPING.get(diff, 0)

    # Calculate Real Boss LV
    boss_lv = party_avg_lv + lv_diff_rate

    # If calculated LV is 0 or less, flag an error an find the floor difficulty for that party.
    if boss_lv <= 0:
        least_diff = ""
        for diff_name, lv in DIFF_TO_LV_MAPPING.items():
            if party_avg_lv + lv > 0:
                least_diff = diff_name
                break

        print("Error: Too low difficulty!")
        print(f"For LV {party_avg_lv} party, "
              f"Boss Difficulty must be at least on {least_diff.capitalize()}.")
        return None

    # Determine Boss' HP
    if boss_lv <= 30:
        boss_hp = (party_avg_lv + hp_diff_rate) * player_num * EARLY_BOSS_HP_MTP
    elif boss_lv <= 60:
        boss_hp = (party_avg_lv + hp_diff_rate) * player_num * MID_BOSS_HP_MTP
    else:
        boss_hp = (party_avg_lv + hp_diff_rate) * player_num * LATE_BOSS_HP_MTP

    # Determine Boss Stats' Roll Point
    boss_stat_pt = boss_lv if boss_lv >= 10 else boss_lv * 5
    boss_stat_mtp = 100 if boss_lv >= 10 else 20

    # Calculate XP Reward
    xp_reward = boss_lv * XP_MULTIPLIER

    # Calculate Money Reward
    money_reward = (party_avg_lv + money_diff_rate) * MONEY_MULTIPLIER

    # Initial Variable Setup
    boss_patk = 0
    boss_matk = 0
    boss_pdef = 0
    boss_mdef = 0

    count = 0

    # Randomize Stat Points
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

    # Show stats if set enabled
    if show_stat:
        print("-------------------------------------------------")
        print(f"BOSS - LV. {boss_lv}")
        if input_diff:
            print(f"{diff.upper()} DIFFICULTY")
        print()
        print("STATS:")
        print(f"HP: {boss_hp}")
        print(f"P. ATK: {boss_patk}")
        print(f"M. ATK: {boss_matk}")
        print(f"P. DEF: {int(boss_pdef / 2)}")
        print(f"M. DEF: {int(boss_mdef / 2)}")
        print("-------------------------------------------------")
        print("Rewards* :")
        print(
            f" • {xp_reward} XP\n"
            f" • {money_reward} (C)\n"
            f" • {item_reward} Item(s)\n"
        )
        print("* Rewards on a scenario case that no one died,\n"
              "and no +20% Bonus from declining dropped item.")
        print("-------------------------------------------------")

    return {
        "LV": boss_lv,
        "HP": boss_hp,
        "PATK": boss_patk,
        "MATK": boss_matk,
        "PDEF": boss_pdef,
        "MDEF": boss_mdef
    }


def random_boss_stat_multi(party_avg_lv, player_num, qty, diff=None, show_stat=True):

    input_diff = True

    # Default value for diff if unspecified
    if diff is None:
        input_diff = False
        diff = "normal"

    # Get Boss LV Difficulty Rate
    lv_diff_rate = DIFF_TO_LV_MAPPING.get(diff, 0)

    # Get Boss HP Difficulty Rate
    hp_diff_rate = DIFF_TO_HP_MAPPING.get(diff, 0)

    # Find Bosses' Real LV
    boss_lv = party_avg_lv + lv_diff_rate

    # If calculated LV is 0 or less, flag an error an find the floor difficulty for that party.
    if boss_lv <= 0:
        least_diff = ""
        for diff_name, lv in DIFF_TO_LV_MAPPING.items():
            if party_avg_lv + lv > 0:
                least_diff = diff_name
                break

        print("Error: Too low difficulty!")
        print(f"For LV {party_avg_lv} party,"
              f"Boss Difficulty must be at least on {least_diff.capitalize()}.")
        return None

    # Calculate XP Reward
    xp_reward = boss_lv * XP_MULTIPLIER

    # Get Boss Coin Reward Difficulty Rate
    money_diff_rate = DIFF_TO_COIN_MAPPING.get(diff, 0)

    # Get Boss Item Reward Difficulty Rate
    item_reward = DIFF_TO_ITEM_MAPPING.get(diff, 0)

    # Calculate Money Reward
    money_reward = (party_avg_lv + money_diff_rate) * MONEY_MULTIPLIER

    # Determine Bosses' HP
    if boss_lv <= 30:
        boss_hp = int(((party_avg_lv + hp_diff_rate) * player_num * EARLY_BOSS_HP_MTP) / 3)
    elif boss_lv <= 60:
        boss_hp = int(((party_avg_lv + hp_diff_rate) * player_num * MID_BOSS_HP_MTP) / 3)
    else:
        boss_hp = int(((party_avg_lv + hp_diff_rate) * player_num * LATE_BOSS_HP_MTP) / 3)

    # Initial Variable Setup
    boss_list = []
    count = 0
    reduce_mtp = 0.8

    while count < qty:
        single_boss_stat = random_boss_stat(party_avg_lv, player_num, diff=diff, show_stat=False)
        current_boss = {
            "LV": single_boss_stat["LV"],
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
        print("   -------- MULTI-BOSS FIGHT --------    ")
        if input_diff:
            print(f"{diff.upper()} DIFFICULTY")
        print()
        for boss in boss_list:
            print(f"Boss #{boss_count} Stats:")
            for stat, value in boss.items():
                if stat == "LV":
                    print(f"LV. {value}")
                elif stat == "PDEF" or stat == "MDEF":
                    print(f"{stat}: {int(value / 2)}")
                else:
                    print(f"{stat}: {value}")

            print()
            boss_count += 1
        print("-------------------------------------------------")
        print("Rewards* :")
        print(
            f" • {xp_reward} XP\n"
            f" • {money_reward} (C)\n"
            f" • {item_reward} Item(s)\n"
        )
        print("* Rewards on a scenario case that no one died,\n"
              "and no +20% Bonus from declining dropped item.\n")
        print("**********************************************")

    return boss_list
