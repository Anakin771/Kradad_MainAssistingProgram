"""
***********************************************

Author: MontyGUI

Description:
This script extends bossPage.py and is a child section of boss_generate_boss.py,
it includes the layout and functions of the interface
that receives user's input for generating boss fights

***********************************************
"""
import tkinter as tk
from tkinter import ttk, messagebox
import sys

# Non-Builtin Imports
from bossStat import *


class BossInputUI:
    def __init__(self, root, frame, reward_cal_ui=None, boss_display_ui=None):
        self.root = root
        self.frame = frame
        self.reward_cal_ui = reward_cal_ui
        self.boss_display_ui = boss_display_ui

        self.validate_func = (self.root.register(self.validate_num), '%P')

        # Party's Average LV
        # Label
        ttk.Label(self.frame, text="Party's Average LV: ", style="category_txt.TLabel").grid(column=0, row=0)
        # Input Spinbox
        self.pal_init = tk.StringVar(self.frame)
        self.pal_init.set("1")
        self.party_avg_lv_box = ttk.Spinbox(
            self.frame,
            from_=1,
            to=sys.maxsize,
            textvariable=self.pal_init,
            validate="key",
            validatecommand=self.validate_func
        )
        self.party_avg_lv_box.grid(column=1, row=0, padx=10, pady=5)

        # Party Size
        # Label
        ttk.Label(self.frame, text="Party Size: ", style="category_txt.TLabel").grid(column=0, row=1)
        # Input Spinbox
        self.ps_init = tk.StringVar(self.frame)
        self.ps_init.set("1")
        self.party_size_box = ttk.Spinbox(
            self.frame,
            from_=1,
            to=sys.maxsize,
            textvariable=self.ps_init,
            validate="key",
            validatecommand=self.validate_func
        )
        self.party_size_box.grid(column=1, row=1, padx=10, pady=5)

        # Boss Number
        # Label
        ttk.Label(self.frame, text="No. of Bosses: ", style="category_txt.TLabel").grid(column=0, row=2)
        # Input Spinbox
        self.bn_init = tk.StringVar(self.frame)
        self.bn_init.set("1")
        self.boss_n_box = ttk.Spinbox(
            self.frame,
            from_=1,
            to=sys.maxsize,
            textvariable=self.bn_init,
            validate="key",
            validatecommand=self.validate_func
        )
        self.boss_n_box.grid(column=1, row=2, padx=10, pady=5)

        # Boss Difficulty
        # Label
        ttk.Label(self.frame, text="Difficulty: ", style="category_txt.TLabel").grid(column=0, row=3)
        # Input Combobox
        self.boss_difficulty_box = ttk.Combobox(
            self.frame,
            state="readonly",
            value=("Noob", "Easy", "Normal", "Hard", "Hardcore")
        )
        self.boss_difficulty_box.current(2)
        self.boss_difficulty_box.grid(column=1, row=3, padx=10, pady=5)

        # Buttons
        # Clear Button
        self.clear_btn = ttk.Button(self.frame, text="Clear", width=20, command=lambda: self.clear())
        self.clear_btn.grid(column=0, row=4, pady=10, ipady=5)

        # Generate Button
        self.generate_btn = ttk.Button(self.frame, text="Generate!", width=20, command=lambda: self.generate_boss())
        self.generate_btn.grid(column=1, row=4, pady=10, ipady=5)

        self.party_avg_lv_box.configure(font=("Helvetica", 11, "bold"))
        self.party_size_box.configure(font=("Helvetica", 11, "bold"))
        self.boss_n_box.configure(font=("Helvetica", 11, "bold"))

    def clear(self):
        self.pal_init.set("1")
        self.ps_init.set("1")
        self.bn_init.set("1")
        self.boss_difficulty_box.current(2)

    def generate_boss(self):
        """
        Event Method that calls when "Generate" Button is clicked,
        generate a boss-fight based on parameters given in the Form.
        The generated Fight is also sent to display and reward calculation.

        :return: False, only if one of the inputs is invalid.
        """
        # Retrieve Input
        pal = int(self.party_avg_lv_box.get())
        ps = int(self.party_size_box.get())
        bn = int(self.boss_n_box.get())
        difficulty = self.boss_difficulty_box.get().lower()

        # Verify Input
        if pal <= 0:
            messagebox.showerror(title="Invalid Input", message="Error!\n'Party's Average LV' must not less than 1!")
            return False
        elif ps <= 0:
            messagebox.showerror(title="Invalid Input", message="Error!\n'Party Size' must not less than 1!")
            return False
        elif bn <= 0:
            messagebox.showerror(title="Invalid Input", message="Error!\n'Boss Number' must not less than 1!")
            return False

        # Check if the boss difficulty is too low
        diff_pass = self.test_difficulty(difficulty, pal)
        if not diff_pass:
            return False

        # Least Difficulty Passed, Generate Boss
        if bn == 1:
            boss = random_boss_stat(pal, ps, difficulty, show_stat=False)
        else:
            boss = random_boss_stat_multi(pal, ps, bn, difficulty, show_stat=False)

        # Send Generated Boss Fight into Display and Reward Calculation
        self.boss_display_ui.display(boss)
        self.reward_cal_ui.calculate(boss, pal)

    @staticmethod
    def test_difficulty(diff: str, pal: int):
        """
        Test the sample party's average level and selected difficulty

        :param diff: Selected difficulty
        :param pal: Stands for Party's Average Level
        :return: True if the selected difficulty generates a boss with non-zero-non-negative stats for that PAL,
            False Otherwise.
        """
        test_result = adjust_difficulty(pal, diff, show_text=False)

        if test_result[1] is None:
            least_diff = ""
            for diff_name, lv in DIFF_TO_LV_MAPPING.items():
                if pal + lv > 0:
                    least_diff = diff_name
                    break
            messagebox.showerror(
                title="Too Low Difficulty",
                message="Error: Too low difficulty!\n"
                        f"For LV {pal} party,\n"
                        f"Boss Difficulty must be at least on {least_diff.capitalize()}."
            )
            return False
        return True

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
