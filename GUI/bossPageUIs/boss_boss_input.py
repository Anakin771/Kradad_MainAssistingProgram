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
        ttk.Label(self.frame, text="Party's Average LV: ").grid(column=0, row=0)
        # Input Spinbox
        pal_init = tk.StringVar(self.frame)
        pal_init.set("1")
        self.party_avg_lv_box = ttk.Spinbox(self.frame, from_=1, to=sys.maxsize, textvariable=pal_init)
        self.party_avg_lv_box.grid(column=1, row=0)

        # Party Size
        # Label
        ttk.Label(self.frame, text="Party Size: ").grid(column=0, row=1)
        # Input Spinbox
        ps_init = tk.StringVar(self.frame)
        ps_init.set("1")
        self.party_size_box = ttk.Spinbox(self.frame, from_=1, to=sys.maxsize, textvariable=ps_init)
        self.party_size_box.grid(column=1, row=1)

        # Boss Number
        # Label
        ttk.Label(self.frame, text="No. of Bosses: ").grid(column=0, row=2)
        # Input Spinbox
        bn_init = tk.StringVar(self.frame)
        bn_init.set("1")
        self.party_avg_lv_box = ttk.Spinbox(self.frame, from_=1, to=sys.maxsize, textvariable=bn_init)
        self.party_avg_lv_box.grid(column=1, row=2)
