"""
***********************************************

Author: MontyGUI

Description
This script includes the GUI of the Player Page,
which includes the functionality like the bossStat.py
scripts found within this project, but operates in a GUI fashion

***********************************************
"""
import tkinter as tk
from tkinter import ttk

# Non-Builtin Imports
from GUI.bossPageUIs.boss_generate_boss import *


class BossPage:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Widget Framework

        # Container Frame
        self.container = ttk.Frame(self.frame)
        self.container.pack(padx=10, pady=10, fill="both")

        # Generate Boss Fight Section
        self.generate_boss_frame = ttk.Frame(self.container)
        self.generate_boss_frame.grid(column=0, row=0)
        self.generate_boss = GenerateBossUI(self.container, self.generate_boss_frame)

        ttk.Separator(self.container).grid(column=0, row=1, sticky="we")

        # Boss Display Section
        self.boss_display_frame = ttk.Frame(self.container)
        self.boss_display_frame.grid(column=0, row=2)
        # self.boss_display = BossDisplayUI(self.container, self.boss_display_frame)

        # TODO: Co-Link Boss-Input to Reward-Cal and Boss-Display
