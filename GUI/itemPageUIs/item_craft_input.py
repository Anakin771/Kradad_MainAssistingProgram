"""
***********************************************

Author: MontyGUI

Description:
This script extends itemPage.py and is a child section of item_craft_item.py,
it includes the layout and functions of the interface
that inputs information necessary to craft an item

***********************************************
"""

import sys
import tkinter as tk
from tkinter import ttk, messagebox

# Non-Builtin Imports
from itemStat import craft_item

ITEM_TYPE_MAPPING = {
    "weapon": "wpn",
    "armor": "amr",
    "accessories": "acc"
}


class CraftInputUI:
    def __init__(self, root, frame, version, craft_display_ui):
        self.root = root
        self.frame = frame
        self.VERSION = version
        self.craft_display_ui = craft_display_ui

        self.validate_func = (self.root.register(self.validate_num), '%P')

        # Player LV
        # Label
        ttk.Label(self.frame, text="Character's LV: ", style="category_txt.TLabel") \
            .grid(column=0, row=0, pady=10)
        # Spinbox
        self.player_lv_init = tk.StringVar(self.frame)
        self.player_lv_init.set("1")
        self.player_lv_box = ttk.Spinbox(
            self.frame,
            from_=1,
            to=sys.maxsize,
            textvariable=self.player_lv_init,
            width=14,
            validate="key",
            validatecommand=self.validate_func
        )
        self.player_lv_box.grid(column=1, row=0, pady=10)

        # Material A
        ttk.Label(self.frame, text="Material #1: ", style="category_txt.TLabel") \
            .grid(column=0, row=1, pady=10)
        self.mat_a_box = ttk.Combobox(self.frame, value=("Weapon", "Armor", "Accessories"), width=14, state="readonly")
        self.mat_a_box.grid(column=1, row=1, pady=10)

        # Material B
        ttk.Label(self.frame, text="Material #2: ", style="category_txt.TLabel") \
            .grid(column=0, row=2, pady=10)
        self.mat_b_box = ttk.Combobox(self.frame, value=("Weapon", "Armor", "Accessories"), width=14, state="readonly")
        self.mat_b_box.grid(column=1, row=2, pady=10)

        # Material C
        ttk.Label(self.frame, text="Material #3: ", style="category_txt.TLabel") \
            .grid(column=0, row=3, pady=10)
        self.mat_c_box = ttk.Combobox(self.frame, value=("Weapon", "Armor", "Accessories"), width=14, state="readonly")
        self.mat_c_box.grid(column=1, row=3, pady=10)

        # Clear Button
        self.clear_btn = ttk.Button(self.frame, text="Clear", width=20, command=lambda: self.clear())
        self.clear_btn.grid(column=0, row=4, padx=8, pady=5, ipady=4)

        # Generate Button
        self.craft_btn = ttk.Button(self.frame, text="Craft!", width=20, command=lambda: self.craft())
        self.craft_btn.grid(column=1, row=4, padx=8, pady=5, ipady=4)

        # Styling
        self.player_lv_box.configure(font=("Helvetica", 11, "bold"))
        self.mat_a_box.configure(font=("Helvetica", 11, "bold"))
        self.mat_b_box.configure(font=("Helvetica", 11, "bold"))
        self.mat_c_box.configure(font=("Helvetica", 11, "bold"))

    def clear(self):
        self.player_lv_init.set("1")
        self.mat_a_box.set("")
        self.mat_b_box.set("")
        self.mat_c_box.set("")

    def craft(self):
        # Retrieve Input
        item_lv = int(self.player_lv_init.get())
        mat_a_raw = self.mat_a_box.get().lower()
        mat_b_raw = self.mat_b_box.get().lower()
        mat_c_raw = self.mat_c_box.get().lower()

        mat_a = ITEM_TYPE_MAPPING.get(mat_a_raw)
        mat_b = ITEM_TYPE_MAPPING.get(mat_b_raw)
        mat_c = ITEM_TYPE_MAPPING.get(mat_c_raw)

        # Validate Input
        if item_lv <= 0:
            messagebox.showerror(title="Invalid Input", message="Error!\n 'Character's LV' must not less than 1!")
            return None
        elif mat_a is None or mat_b is None or mat_c is None:
            messagebox.showerror(title="Invalid Input", message="Error!\nPlease fill in all of your material's type!")
            return None

        # Generate Crafted Item & Display
        item = craft_item(mat_a, mat_b, mat_c, item_lv, show_stat=False)
        self.craft_display_ui.animate(lambda: self.craft_display_ui.display(item))

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
