"""
***********************************************

Author: MontyGUI

Description
This script extends playerPage.py,
it includes the layout and functions of the interface
that guides the user into generating a new character stats.
***********************************************
"""
import tkinter as tk
from tkinter import ttk

# Non-builtin Imports:
from GUI.playerPageUIs.player_nc_starting import *
from GUI.playerPageUIs.player_nc_bonus import *


class NewCharUI:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # New Char - Header
        self.new_char_header_frame = ttk.Frame(self.frame)
        self.new_char_header_frame.grid(column=0, row=0)

        # Title
        ttk.Label(self.new_char_header_frame, text="New Character", style="tab_header.TLabel")\
            .grid(column=0, row=0, sticky="s")

        # Subtitle
        ttk.Label(self.new_char_header_frame,
                  text="Generate your new character's Stat Points here!",
                  style="tab_subtitle.TLabel").grid(column=1, row=0, sticky="s", padx=10, pady=5)

        # Main Context Frame
        self.new_char_content_frame = ttk.Frame(self.frame)
        self.new_char_content_frame.grid(column=0, row=1)
        # Starting Stats Section
        # Detailed Code in player_nc_starting.py
        self.starting_stat_frame = ttk.Frame(self.new_char_content_frame)
        self.starting_stat_frame.grid(column=0, row=0)
        self.starting_stats = StartingStatsUI(self.new_char_content_frame, self.starting_stat_frame)

        # Steps Separator
        ttk.Separator(self.new_char_content_frame, orient="vertical")\
            .grid(column=1, row=0, padx=35, sticky="ns")

        # Bonus Rate Section
        self.bonus_rate_frame = ttk.Frame(self.new_char_content_frame)
        self.bonus_rate_frame.grid(column=2, row=0)
        self.bonus_rate = BonusRateUI(self.new_char_content_frame, self.bonus_rate_frame)

        # EXTRA: Starting Stats & Bonus Rate UI Linking
        self.starting_stats.bnrp_ui = self.bonus_rate
        self.bonus_rate.strts_ui = self.starting_stats
