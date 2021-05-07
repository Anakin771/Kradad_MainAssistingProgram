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
from tkinter import ttk
import sys


class BossInputUI:
    def __init__(self, root, frame, reward_cal_ui=None, boss_display_ui=None):
        self.root = root
        self.frame = frame
        self.reward_cal_ui = reward_cal_ui
        self.boss_display_ui = boss_display_ui

        # Party's Average LV
        # Label
        ttk.Label(self.frame, text="Party's Average LV: ", style="category_txt.TLabel").grid(column=0, row=0)
        # Input Spinbox
        self.pal_init = tk.StringVar(self.frame)
        self.pal_init.set("1")
        self.party_avg_lv_box = ttk.Spinbox(self.frame, from_=1, to=sys.maxsize, textvariable=self.pal_init)
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
            textvariable=self.ps_init
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
            textvariable=self.bn_init
        )
        self.boss_n_box.grid(column=1, row=2, padx=10, pady=5)

        # Boss Difficulty
        # Label
        ttk.Label(self.frame, text="Difficulty: ", style="category_txt.TLabel").grid(column=0, row=3)
        # Input Combobox
        self.boss_difficulty_box = ttk.Combobox(
            self.frame,
            value=("Noob", "Easy", "Normal", "Hard", "Hardcore")
        )
        self.boss_difficulty_box.current(2)
        self.boss_difficulty_box.grid(column=1, row=3, padx=10, pady=5)

        # Buttons
        # Clear Button
        self.clear_btn = ttk.Button(self.frame, text="Clear", width=20)
        self.clear_btn.grid(column=0, row=4, pady=10, ipady=5)

        # Generate Button
        self.generate_btn = ttk.Button(self.frame, text="Generate!", width=20)
        self.generate_btn.grid(column=1, row=4, pady=10, ipady=5)

        self.party_avg_lv_box.configure(font=("Helvetica", 11, "bold"))
        self.party_size_box.configure(font=("Helvetica", 11, "bold"))
        self.boss_n_box.configure(font=("Helvetica", 11, "bold"))
