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
from tkinter import ttk, messagebox
import sys

# Non-builtin Imports:
from playerStat import calculate_level_up

TXT_TO_BOOL_ITEM_BONUS_MAPPING = {
    "accepted": True,
    "declined": False,
    "none": True
}


class LevelUpInputUI:
    def __init__(self, root, frame, version, lvl_display_ui=None):
        self.root = root
        self.frame = frame
        self.VERSION = version
        self.lvl_display_ui = lvl_display_ui

        self.validate_func = (self.root.register(self.validate_num), '%P')

        input_fonts = ("Helvetica", 11, "bold")

        # Category Texts

        # Current LV
        ttk.Label(self.frame, text="Current LV: ", style="lu_category.TLabel").grid(column=0, row=0)
        # Current Remainder XP
        ttk.Label(self.frame, text="Remainder XP: ", style="lu_category.TLabel").grid(column=0, row=1)
        # Gained XP
        ttk.Label(self.frame, text="Gained XP: ", style="lu_category.TLabel").grid(column=0, row=2)
        # Fallen Ally
        ttk.Label(self.frame, text="No. of Fallen Ally: ", style="lu_category.TLabel").grid(column=0, row=3)

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
            textvariable=self.current_lv_init,
            validate="key",
            validatecommand=self.validate_func
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
            textvariable=self.rem_xp_init,
            validate="key",
            validatecommand=self.validate_func
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
            textvariable=self.gained_xp_init,
            validate="key",
            validatecommand=self.validate_func
        )
        self.gained_xp_box.grid(column=1, row=2, padx=15, pady=5)

        # Fallen Ally Initial Input
        self.fallen_init = tk.StringVar(self.frame)
        self.fallen_init.set("0")
        # Fallen Ally Input
        self.fallen_box = ttk.Spinbox(
            self.frame,
            from_=0,
            to=sys.maxsize,
            width=10,
            textvariable=self.fallen_init,
            validate="key",
            validatecommand=self.validate_func
        )
        self.fallen_box.grid(column=1, row=3, padx=15, pady=5)

        self.current_lv_box.configure(font=input_fonts)
        self.rem_xp_box.configure(font=input_fonts)
        self.gained_xp_box.configure(font=input_fonts)
        self.fallen_box.configure(font=input_fonts)

        # Dropped Item Options
        # Header
        ttk.Label(self.frame, text="Dropped Item: ", style="lu_category.TLabel").grid(column=0, row=4, pady=5)
        # Radio Buttons Frame
        self.drp_itm_rd_frame = ttk.Frame(self.frame, relief="groove")
        self.drp_itm_rd_frame.grid(column=0, columnspan=2, row=5, padx=20, pady=3)

        # Radio Buttons
        # Option Variable
        self.item_accepted = tk.StringVar(self.frame, "accepted")
        # Item Accepted
        self.drp_itm_acc = ttk.Radiobutton(
            self.drp_itm_rd_frame,
            variable=self.item_accepted,
            text="Accept",
            value="accepted"
        )
        self.drp_itm_acc.grid(column=0, row=0, padx=10, pady=5)
        # Item Declined
        self.drp_itm_decl = ttk.Radiobutton(
            self.drp_itm_rd_frame,
            variable=self.item_accepted,
            text="Decline",
            value="declined"
        )
        self.drp_itm_decl.grid(column=1, row=0, padx=10, pady=5)
        # No Item (Boss Rewards 0 items)
        self.drp_no_item = ttk.Radiobutton(
            self.drp_itm_rd_frame,
            variable=self.item_accepted,
            text="No Item*",
            value="none"
        )
        self.drp_no_item.grid(column=2, row=0, padx=10, pady=5)

        # No Item Footnote
        ttk.Label(self.frame, text="* Select this if the boss drops no item as a reward.")\
            .grid(column=0, columnspan=2, row=6, pady=3)

        # Form/Button Separator
        ttk.Separator(self.frame).grid(column=0, columnspan=2, row=7, pady=6, sticky="we")

        # Clear Button
        self.clear_btn = ttk.Button(self.frame, text="Clear", width=20, command=lambda: self.clear())
        self.clear_btn.grid(column=0, row=8, pady=8, ipady=4)

        # Calculate Button
        self.calculate_btn = ttk.Button(
            self.frame,
            text="Calculate!",
            width=20,
            command=lambda: self.calculate_lvl()
        )
        self.calculate_btn.grid(column=1, row=8, pady=8, ipady=4)

    def clear(self):
        self.current_lv_init.set("1")
        self.rem_xp_init.set("0")
        self.gained_xp_init.set("1")
        self.fallen_init.set("0")
        self.current_lv_box.configure(textvariable=self.current_lv_init)
        self.rem_xp_box.configure(textvariable=self.rem_xp_init)
        self.gained_xp_box.configure(textvariable=self.gained_xp_init)
        self.fallen_box.configure(textvariable=self.fallen_init)
        self.drp_itm_acc.invoke()

    def calculate_lvl(self):

        # Retrieve inputs
        char_lv = int(self.current_lv_box.get())
        rem_xp = int(self.rem_xp_box.get())
        gained_xp = int(self.gained_xp_box.get())
        fallen = int(self.fallen_box.get())
        item_choice = TXT_TO_BOOL_ITEM_BONUS_MAPPING.get(self.item_accepted.get(), None)

        # Validate Input
        if char_lv <= 0:
            messagebox.showerror(title="Invalid Input", message="Error!\n'Current LV' must not less than 1!")
            return False
        if rem_xp < 0:
            messagebox.showerror(title="Invalid Input", message="Error!\n'Remainder XP' must not less than 0!")
            return False
        if gained_xp <= 0:
            messagebox.showerror(title="Invalid Input", message="Error!\n'Gained XP' must not less than 1!")
            return False
        if fallen < 0:
            messagebox.showerror(title="Invalid Input", message="Error!\n'No. of Fallen Ally' must not less than 0!")
            return False
        if item_choice is None:
            messagebox.showerror(title="Invalid Input", message="Error!\nPlease select an option in 'Dropped item'!")
            return False

        lvl_progress = calculate_level_up(char_lv, rem_xp, gained_xp, fallen, item_choice, show_stat=False)

        self.lvl_display_ui.display(lvl_progress)

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
