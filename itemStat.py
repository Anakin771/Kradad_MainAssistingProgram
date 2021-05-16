"""
***********************************************

Author: MontyGUI

Description
This script includes every functions that revolves around
generating items, including stats randomization, item crafting, etc.

***********************************************
"""

import numpy as np
import random
import math

QUALITY_MAPPING = {}
QUALITY_MAPPING.update(dict.fromkeys([1, 2, 3, 18, 19, 20], -7))  # Bad Quality
QUALITY_MAPPING.update(dict.fromkeys(range(6, 16), 0))  # Normal Quality
QUALITY_MAPPING.update(dict.fromkeys([4, 5, 16, 17], 7))  # Great Quality

QUALITY_TEXT_MAPPING = {
    -7: "BAD",
    0: "NORMAL",
    7: "GREAT"
}

MATERIAL_TYPE_MAPPING = {
    "wpn": 1,
    "amr": 10,
    "acc": 100
}

CRAFT_TYPE_MAPPING = {
    3: "wpn",
    30: "amr",
    300: "acc"
}

ITEM_TYPE_MAPPING = {
    "wpn": "Weapon",
    "amr": "Armor",
    "acc": "Accessories"
}

WPN_WEIGHT = [12, 32, 32, 12, 12]  # Weapon Random Weight
AMR_WEIGHT = [26, 11, 11, 26, 26]  # Armor Random Weight

DEVIATION = 12


def random_item_stat(item_lv, item_type, quality_rate=None, show_stat=True):
    """
    Random the stats for an item
    :param item_lv:
    :param item_type:
    :param quality_rate:
    :param show_stat:
    :return:
    """

    if quality_rate is None:
        quality_rate = 0
        quality_text = ""
    else:
        if QUALITY_TEXT_MAPPING.get(quality_rate, None) is None:
            print("Sorry, you do not input the right quality rate!")
            return None
        quality_text = f"{QUALITY_TEXT_MAPPING.get(quality_rate, None)} QUALITY "

    # Set the number of Stat Roll: Item's LV * 5 for LV 1-9, and Item's LV for LV 10+
    # Also, if the item has quality rate, it is also added to the roll point here
    item_stat_pt = (item_lv + quality_rate) if item_lv >= 10 else (item_lv + quality_rate) * 5

    # Set the number of Stat Point Multiplier: 10 for LV 1-9, and 50 for LV 10+
    item_stat_mtp = 50 if item_lv >= 10 else 10

    roll_choice = ["HP", "PATK", "MATK", "PDEF", "MDEF"]

    if item_type == "wpn":
        rand_variant = np.round(np.random.normal(0, DEVIATION, size=1))[0]
        variant = int(min(np.abs(rand_variant), 32))
        variant = int(math.copysign(variant, rand_variant))
        roll_weight = WPN_WEIGHT
        roll_weight[1] += variant
        roll_weight[2] -= variant
    elif item_type == "amr":
        roll_weight = AMR_WEIGHT
    else:
        roll_weight = [20, 20, 20, 20, 20]

    # Build Item's Stat Points dictionary
    item = {
        "LV": item_lv,
    }

    if item_type is not None:
        item.update({"TYPE": item_type})

    if quality_rate is not None:
        item.update({"QUALITY": quality_rate})

    item.update({
        "HP": 0,
        "PATK": 0,
        "MATK": 0,
        "PDEF": 0,
        "MDEF": 0
    })

    # Random the category for the current stat point
    item_rand = random.choices(roll_choice, weights=roll_weight, k=item_stat_pt)
    for stat in item_rand:
        item[stat] += 1 * item_stat_mtp

    # Display the stat (if needed)
    if show_stat:
        item_type_text = f"{ITEM_TYPE_MAPPING.get(item_type).upper()} - " if item_type is not None else ""

        print("---------------------------------")
        print(f" ITEM STAT POINTS\n({quality_text}{item_type_text}LV. {item_lv})")
        print(f" HP: +{item['HP']} pts.")
        print(f" P. ATK: +{item['PATK']} pts.")
        print(f" M. ATK: +{item['MATK']} pts.")
        print(f" P. DEF: +{item['PDEF']} pts.")
        print(f" M. DEF: +{item['MDEF']} pts.")
        print("---------------------------------")

    return item


def craft_item(material_a, material_b, material_c, player_lv):
    """
    Craft an item based on given material type
    :param material_a:
    :param material_b:
    :param material_c:
    :param player_lv:
    :return:
    """
    type_sum =\
        MATERIAL_TYPE_MAPPING.get(material_a, -1000) \
        + MATERIAL_TYPE_MAPPING.get(material_b, -1000) \
        + MATERIAL_TYPE_MAPPING.get(material_c, -1000)

    if type_sum < 0:
        print("Sorry, you didn't input all material types correctly.")
        return None

    crafted_type = CRAFT_TYPE_MAPPING.get(type_sum, random.choice(["wpn", "amr", "acc"]))
    crafted_quality = QUALITY_MAPPING.get(random.randint(1, 20))

    crafted_item = random_item_stat(
        player_lv,
        quality_rate=crafted_quality,
        item_type=crafted_type,
    )

    return crafted_item
