"""
***********************************************

Author: MontyGUI

Description:
This script extends itemPage.py and is a child section of item_dropped_item.py,
it includes the layout and functions of the interface
that inputs information necessary to generate boss dropped item

***********************************************
"""

import sys
import tkinter as tk
from tkinter import ttk, messagebox

# Non-Builtin Imports
from itemStat import random_item_stat

ITEM_TYPE_MAPPING = {
    "weapon": "wpn",
    "armor": "amr",
    "accessories": "acc"
}


class DroppedInputUI:
    def __init__(self, root, frame, display_ui):
        self.root = root
        self.frame = frame
        self.display_ui = display_ui

        self.validate_func = (self.root.register(self.validate_num), '%P')

        # Boss LV
        # Label
        ttk.Label(self.frame, text="Boss LV: ", style="category_txt.TLabel")\
            .grid(column=0, row=0, pady=10)
        # Spinbox
        self.boss_lv_init = tk.StringVar(self.frame)
        self.boss_lv_init.set("1")
        self.boss_lv_box = ttk.Spinbox(
            self.frame,
            from_=1,
            to=sys.maxsize,
            textvariable=self.boss_lv_init,
            width=15
        )
        self.boss_lv_box.grid(column=1, row=0, pady=10)

        # Item Type
        ttk.Label(self.frame, text="Item Type: ", style="category_txt.TLabel") \
            .grid(column=0, row=1, pady=10)
        self.item_type_box = ttk.Combobox(
            self.frame,
            value=("Weapon", "Armor", "Accessories"),
            width=15,
            state="readonly"
        )
        self.item_type_box.grid(column=1, row=1, pady=10)

        # Clear Button
        self.clear_btn = ttk.Button(self.frame, text="Clear", width=20, command=lambda: self.clear())
        self.clear_btn.grid(column=0, row=2, padx=8, pady=5, ipady=8)

        # Generate Button
        self.generate_btn = ttk.Button(self.frame, text="Generate!", width=20, command=lambda: self.generate_item())
        self.generate_btn.grid(column=1, row=2, padx=8, pady=5, ipady=8)

        # Styling
        self.boss_lv_box.configure(font=("Helvetica", 11, "bold"))
        self.item_type_box.configure(font=("Helvetica", 11, "bold"))

    def clear(self):
        self.boss_lv_init.set("1")
        self.item_type_box.set("")

    def generate_item(self):
        # Retrieve Input
        item_lv = int(self.boss_lv_box.get())
        item_type_raw = str(self.item_type_box.get()).lower()
        item_type = ITEM_TYPE_MAPPING.get(item_type_raw, "")

        # Validate Input
        if item_lv <= 0:
            messagebox.showerror(title="Invalid Input", message="Error!\n 'Item LV' must not less than 1!")
            return None
        elif item_type not in ("wpn", "amr", "acc"):
            messagebox.showerror(title="Invalid Input", message="Error!\n Please choose the item type!")
            return None

        # Generate Item & Display
        item = random_item_stat(item_lv, item_type, show_stat=False)
        self.display_ui.display(item)

    @staticmethod
    def validate_num(data_in):
        if data_in.isdigit():
            return True
        elif data_in == "":
            # Blank String
            return True
        else:
            # NaN
            return False
