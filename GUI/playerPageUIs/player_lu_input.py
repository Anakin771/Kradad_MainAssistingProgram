"""
***********************************************

Author: MontyGUI

Description
This script extends playerPage.py and is a child section of player_level_up.py,
it includes the layout and functions of the interface
that receives user's input for Level calculation.
***********************************************
"""
import tkinter as tk
from tkinter import ttk
import sys

# Non-builtin Imports:


class LevelUpInputUI:
    def __init__(self, root, frame, lvl_display_ui=None):
        self.root = root
        self.frame = frame
        self.lvl_display_ui = lvl_display_ui

        # Category Texts

        # Current LV
        ttk.Label(self.frame, text="Current LV: ", style="lu_category.TLabel").grid(column=0, row=0)
        # Current Remainder XP
        ttk.Label(self.frame, text="Remainder XP: ", style="lu_category.TLabel").grid(column=0, row=1)
        # Gained XP
        ttk.Label(self.frame, text="Gained XP: ", style="lu_category.TLabel").grid(column=0, row=2)

        # Input Boxes
        # Current LV Initial Value
        self.current_lv_init = tk.StringVar(self.frame)
        self.current_lv_init.set("1")
        # Current LV Input
        self.current_lv_box = ttk.Spinbox(
            self.frame,
            from_=1,
            to=sys.maxsize,
            width=10,
            textvariable=self.current_lv_init
        )
        self.current_lv_box.grid(column=1, row=0, padx=15, pady=5)

        # Current Remainder XP Initial Value
        self.rem_xp_init = tk.StringVar(self.frame)
        self.rem_xp_init.set("0")
        # Current Remainder XP Input
        self.rem_xp_box = ttk.Spinbox(
            self.frame,
            from_=0,
            to=sys.maxsize,
            width=10,
            textvariable=self.rem_xp_init
        )
        self.rem_xp_box.grid(column=1, row=1, padx=15, pady=5)

        # Gained XP Initial Value
        self.gained_xp_init = tk.StringVar(self.frame)
        self.gained_xp_init.set("1")
        # Gained XP Input
        self.gained_xp_box = ttk.Spinbox(
            self.frame,
            from_=1,
            to=sys.maxsize,
            width=10,
            textvariable=self.gained_xp_init
        )
        self.gained_xp_box.grid(column=1, row=2, padx=15, pady=5)

        self.current_lv_box.configure(font=("Helvetica", 11, "bold"))
        self.rem_xp_box.configure(font=("Helvetica", 11, "bold"))
        self.gained_xp_box.configure(font=("Helvetica", 11, "bold"))

        # Dropped Item Options
        # Header
        ttk.Label(self.frame, text="Dropped Item: ", style="lu_category.TLabel").grid(column=0, row=3)
        # Radio Buttons Frame
        self.drp_itm_rd_frame = ttk.Frame(self.frame, relief="groove")
        self.drp_itm_rd_frame.grid(column=1, row=3, padx=10, pady=5)

        # Radio Buttons
        # Option Variable
        self.item_accepted = tk.StringVar(self.frame, "1")
        # Item Accepted
        self.drp_itm_acc = ttk.Radiobutton(
            self.drp_itm_rd_frame,
            variable=self.item_accepted,
            text="Accept",
            value="1"
        )
        self.drp_itm_acc.grid(column=0, row=0, padx=15, pady=2)
        # Item Declined
        self.drp_itm_decl = ttk.Radiobutton(
            self.drp_itm_rd_frame,
            variable=self.item_accepted,
            text="Decline",
            value="0"
        )
        self.drp_itm_decl.grid(column=0, row=1, padx=15, pady=2)

        # Clear Button
        self.clear_btn = ttk.Button(self.frame, text="Clear", width=14)
        self.clear_btn.grid(column=0, row=4, pady=10, ipady=4)

        # Calculate Button
        self.calculate_btn = ttk.Button(self.frame, text="Calculate!", width=14)
        self.calculate_btn.grid(column=1, row=4, pady=10, ipady=4)
