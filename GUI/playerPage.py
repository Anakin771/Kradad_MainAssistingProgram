"""
***********************************************

Author: MontyGUI

Description
This script includes the GUI of the Player Page,
which includes the functionality like the playerStat.py
scripts found within this project, but operates in a GUI fashion

***********************************************
"""

# Non-builtin Imports:
from GUI.playerPageUIs.player_new_char import *
from GUI.playerPageUIs.player_level_up import *


class PlayerPage:
    def __init__(self, root, parent, frame, **kwargs):
        self.root = root
        self.parent = parent
        self.frame = frame

        # Widget Framework

        # Container Frame
        self.container = ttk.Frame(self.frame, relief="groove", borderwidth=3)
        self.container.pack(ipadx=10, ipady=20, padx=10, pady=10)

        # New Character Section
        self.new_char_frame = ttk.Frame(self.container)
        self.new_char_frame.grid(column=0, row=0)
        self.new_char = NewCharUI(self.container, self.new_char_frame)

        # Actions Separator
        ttk.Separator(self.container).grid(column=0, row=1, padx=5, pady=25, sticky="we")

        # Level Calculation Section
        self.level_up_frame = ttk.Frame(self.container)
        self.level_up_frame.grid(column=0, row=2)
        self.level_up = CalculateLevelUI(self.container, self.level_up_frame)

