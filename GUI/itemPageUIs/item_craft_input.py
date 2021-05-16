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
from tkinter import ttk


class CraftInputUI:
    def __init__(self, parent, frame):
        self.parent = parent
        self.frame = frame

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
            width=14
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
        self.clear_btn = ttk.Button(self.frame, text="Clear", width=20)
        self.clear_btn.grid(column=0, row=4, padx=8, pady=5, ipady=4)

        # Generate Button
        self.craft_btn = ttk.Button(self.frame, text="Craft!", width=20)
        self.craft_btn.grid(column=1, row=4, padx=8, pady=5, ipady=4)

        # Styling
        self.player_lv_box.configure(font=("Helvetica", 11, "bold"))
        self.mat_a_box.configure(font=("Helvetica", 11, "bold"))
        self.mat_b_box.configure(font=("Helvetica", 11, "bold"))
        self.mat_c_box.configure(font=("Helvetica", 11, "bold"))
