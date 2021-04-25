"""
***********************************************

Author: MontyGUI

Description
This script includes every functions that revolves around
generating items, including stats randomization, item crafting, etc.

***********************************************
"""

import random

QUALITY_MAPPING = {}
QUALITY_MAPPING.update(dict.fromkeys([1, 2, 3, 18, 19, 20], -2))
QUALITY_MAPPING.update(dict.fromkeys(range(6, 16), 0))
QUALITY_MAPPING.update(dict.fromkeys([4, 5, 16, 17], 2))

QUALITY_TEXT_MAPPING = {
    -2: "BAD",
    0: "NORMAL",
    2: "GREAT"
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


def random_item_stat(item_lv, item_type=None, quality_rate=None, show_stat=True):
    """
    Random the stats for an item
    :param item_lv:
    :param quality_rate:
    :param item_type:
    :param show_stat:
    :return:
    """

    if quality_rate is None:
        quality_rate = 0
        quality_text = ""
    else:
        quality_text = f"{QUALITY_TEXT_MAPPING.get(quality_rate, None)} QUALITY "
        if quality_text is None:
            print("Sorry, you do not input the right quality rate!")
            return None

    # Set the number of Stat Roll: Item's LV * 5 for LV 1-9, and Item's LV for LV 10+
    # Also, if the item has quality rate, it is also added to the roll point here
    item_stat_pt = (item_lv + quality_rate) if item_lv >= 10 else (item_lv + quality_rate) * 5

    # Set the number of Stat Point Multiplier: 10 for LV 1-9, and 50 for LV 10+
    item_stat_mtp = 50 if item_lv >= 10 else 10

    # Stat Point Category variable category setup
    item_hp = 0
    item_patk = 0
    item_matk = 0
    item_pdef = 0
    item_mdef = 0

    # While loop counter
    count = 0

    while count < item_stat_pt:
        # Random the category for the current stat point
        item_rand = random.randint(1, 5)

        if item_rand == 1:
            # Add the current pts. to PATK
            item_patk += 1 * item_stat_mtp
        elif item_rand == 2:
            # Add the current pts. to MATK
            item_matk += 1 * item_stat_mtp
        elif item_rand == 3:
            # Add the current pts. to PDEF
            item_pdef += 1 * item_stat_mtp
        elif item_rand == 4:
            # Add the current pts. to MDEF
            item_mdef += 1 * item_stat_mtp
        elif item_rand == 5:
            # Add the current pts. to HP
            item_hp += 1 * item_stat_mtp

        # Counter Up
        count += 1

    # Display the stat (if needed)
    if show_stat:
        item_type_text = f"{ITEM_TYPE_MAPPING.get(item_type).upper()} - " if item_type is not None else ""

        print("---------------------------------")
        print(f"ITEM STAT POINTS\n({quality_text}{item_type_text}LV. {item_lv})")
        print(f"HP: +{item_hp} pts.")
        print(f"P. ATK: +{item_patk} pts.")
        print(f"M. ATK: +{item_matk} pts.")
        print(f"P. DEF: +{int(item_pdef)} pts.")
        print(f"M. DEF: +{int(item_mdef)} pts.")
        print("---------------------------------")

    # Return Item's Stat Points as a dictionary
    item = {
        "LV": item_lv,
    }

    if item_type is not None:
        item.update({"TYPE": item_type})

    if quality_rate is not None:
        item.update({"QUALITY": quality_rate})

    item.update({
        "HP": item_hp,
        "PATK": item_patk,
        "MATK": item_matk,
        "PDEF": item_pdef,
        "MDEF": item_mdef
    })

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
