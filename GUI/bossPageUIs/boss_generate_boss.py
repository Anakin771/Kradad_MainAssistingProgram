"""
***********************************************

Author: MontyGUI

Description
This script extends bossPage.py,
it includes the layout and functions of the interface
generates a boss fight.
***********************************************
"""
import tkinter as tk
from tkinter import ttk

# Non-Builtin Imports
from GUI.bossPageUIs.boss_boss_input import *


class GenerateBossUI:
    def __init__(self, root, frame, boss_display_ui=None):
        self.root = root
        self.frame = frame
        self.boss_display_ui = boss_display_ui

        # Header Frame
        self.header_frame = ttk.Frame(self.frame)
        self.header_frame.grid(column=0, row=0)
        # Heading Text
        ttk.Label(self.header_frame, text="Generate Boss Fight", style="tab_header.TLabel").grid(column=0, row=0)
        ttk.Label(self.header_frame, text="Let the game begin!", style="tab_subtitle.TLabel")\
            .grid(column=1, row=0, sticky="s", padx=10, pady=5)

        # Content Frame
        self.content_frame = ttk.Label(self.frame)
        self.content_frame.grid(column=0, row=1)

        # Content - Input Section
        self.boss_input_frame = ttk.Frame(self.content_frame)
        self.boss_input_frame.grid(column=0, row=0)
        self.boss_input = BossInputUI(self.content_frame, self.boss_input_frame)

        # TODO: Co-Link Boss-Input to Reward-Cal and Boss-Display
