"""
***********************************************

Author: MontyGUI

Description
This script extends playerPage.py,
it includes the layout and functions of the interface
that calculating user's Character LV
***********************************************
"""

from tkinter import ttk

# Non-builtin Imports:
from GUI.playerPageUIs.player_lu_input import LevelUpInputUI
from GUI.playerPageUIs.player_lu_display import LevelUpDisplayUI


class CalculateLevelUI:
    def __init__(self, root, frame, version):
        self.root = root
        self.frame = frame
        self.VERSION = version

        # Heading Text
        ttk.Label(self.frame, text="Calculate Level", style="tab_header.TLabel").\
            grid(column=0, row=0, sticky="s")

        # Subtitle Text
        ttk.Label(self.frame,
                  text="Find out how much you've become stronger!",
                  style="tab_subtitle.TLabel"
                  )\
            .grid(column=1, row=0, sticky="s", padx=10, pady=5)

        # Input Section
        self.lvl_input_frame = ttk.Frame(self.frame)
        self.lvl_input_frame.grid(column=0, row=1, pady=10)
        self.lvl_input = LevelUpInputUI(self.root, self.lvl_input_frame, version=self.VERSION)

        # Display Section
        self.lvl_display_frame = ttk.Frame(self.frame)
        self.lvl_display_frame.grid(column=1, row=1, pady=10)
        self.lvl_display = LevelUpDisplayUI(self.root, self.lvl_display_frame, version=self.VERSION)

        # Input Section & Display Section Linking
        self.lvl_input.lvl_display_ui = self.lvl_display
