"""
***********************************************

Author: MontyGUI

Description:
This script includes the GUI of the Boss Page,
which includes the functionality like the bossStat.py
scripts found within this project, but operates in a GUI fashion

***********************************************
"""

# Non-Builtin Imports
from GUI.bossPageUIs.boss_generate_boss import *
from GUI.bossPageUIs.boss_display import *


class BossPage:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Widget Framework

        # Container Frame
        self.container = ttk.Frame(self.frame, relief="groove", borderwidth=3)
        self.container.pack(padx=10, pady=10, ipadx=10, ipady=10)

        # Boss Display Section
        self.boss_display_frame = ttk.Frame(
            self.container,
            relief="groove",
            borderwidth=4
        )
        self.boss_display = BossDisplayUI(self.container, self.boss_display_frame)

        # Generate Boss Fight Section
        self.generate_boss_frame = ttk.Frame(self.container)
        self.generate_boss = GenerateBossUI(self.container, self.generate_boss_frame, boss_display_ui=self.boss_display)

        # Positioning
        self.generate_boss_frame.pack()
        ttk.Separator(self.container).pack(padx=25, pady=10, expand=True, fill="both")
        self.boss_display_frame.pack(expand=True, fill="both", padx=40, pady=15)
