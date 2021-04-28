"""
***********************************************

Author: MontyGUI

Description
This script extends playerPage.py and is a child section of player_new_char.py,
it includes the layout and functions of the interface
that generates starting stats of a new character.
***********************************************
"""

import tkinter as tk
from tkinter import ttk


class StartingStatsUI:
    def __init__(self, parent, frame, bnrp_ui=None):
        self.parent = parent
        self.frame = frame
        self.bnrp_ui = bnrp_ui

        # Starting Stats - Heading Text
        ttk.Label(
            self.frame,
            text="Step 1 - Generating Starting Stat Points",
            style="strts_text.TLabel"
        ) \
            .grid(column=0, row=0, columnspan=2, pady=10)

        # Starting Stats - Stats Panel
        self.strts_display_panel = ttk.Frame(self.frame)
        self.strts_display_panel.grid(column=0, row=1)

        # Starting Stats - Stats Display
        # Stats Name Label
        ttk.Label(self.strts_display_panel, text="HP: ", style="strts_stat.TLabel").grid(column=0, row=0)
        ttk.Label(self.strts_display_panel, text="P. ATK: ", style="strts_stat.TLabel").grid(column=0, row=1)
        ttk.Label(self.strts_display_panel, text="M. ATK: ", style="strts_stat.TLabel").grid(column=0, row=2)
        ttk.Label(self.strts_display_panel, text="P. DEF: ", style="strts_stat.TLabel").grid(column=0, row=3)
        ttk.Label(self.strts_display_panel, text="M. DEF: ", style="strts_stat.TLabel").grid(column=0, row=4)
        ttk.Label(self.strts_display_panel, text="FREE: ", style="strts_stat.TLabel").grid(column=0, row=5)

        # Stats Number Boxes

        # HP Box
        self.strts_hp_box = ttk.Label(self.strts_display_panel, width=6, relief="sunken")
        self.strts_hp_box.configure(background="white")

        # P. ATK Box
        self.strts_patk_box = ttk.Label(self.strts_display_panel, width=6, relief="sunken")
        self.strts_patk_box.configure(background="white")

        # M. ATK Box
        self.strts_matk_box = ttk.Label(self.strts_display_panel, width=6, relief="sunken")
        self.strts_matk_box.configure(background="white")

        # P. DEF Box
        self.strts_pdef_box = ttk.Label(self.strts_display_panel, width=6, relief="sunken")
        self.strts_pdef_box.configure(background="white")

        # M. DEF Box
        self.strts_mdef_box = ttk.Label(self.strts_display_panel, width=6, relief="sunken")
        self.strts_mdef_box.configure(background="white")

        # FREE Box
        self.strts_free_box = ttk.Label(self.strts_display_panel, width=6, relief="sunken")
        self.strts_free_box.configure(background="white")

        # Alignment
        self.strts_hp_box.grid(column=1, row=0, padx=5)
        self.strts_patk_box.grid(column=1, row=1, padx=5)
        self.strts_matk_box.grid(column=1, row=2, padx=5)
        self.strts_pdef_box.grid(column=1, row=3, padx=5)
        self.strts_mdef_box.grid(column=1, row=4, padx=5)
        self.strts_free_box.grid(column=1, row=5, padx=5)

        # Unit Ending (pts.)
        ttk.Label(self.strts_display_panel, text=" pts.", style="strts_stat.TLabel").grid(column=2, row=0)
        ttk.Label(self.strts_display_panel, text=" pts.", style="strts_stat.TLabel").grid(column=2, row=1)
        ttk.Label(self.strts_display_panel, text=" pts.", style="strts_stat.TLabel").grid(column=2, row=2)
        ttk.Label(self.strts_display_panel, text=" pts.", style="strts_stat.TLabel").grid(column=2, row=3)
        ttk.Label(self.strts_display_panel, text=" pts.", style="strts_stat.TLabel").grid(column=2, row=4)
        ttk.Label(self.strts_display_panel, text=" pts.", style="strts_stat.TLabel").grid(column=2, row=5)
        # END: Starting Stats - Stats Panel

        # Starting Stats - Action Buttons Panel
        self.strts_buttons_frame = ttk.Frame(self.frame)
        self.strts_buttons_frame.grid(column=1, row=1)

        # Starting Stat - Random Button
        # TODO: Insert Random (and Re-Random) command into Random Button
        ttk.Button(self.strts_buttons_frame, text="Random").grid(column=0, row=0, pady=10, ipady=5)
        # TODO: Insert Stat-Locking command into Confirm Button
        ttk.Button(self.strts_buttons_frame, text="Confirm").grid(column=0, row=2, pady=10, ipady=5)

        # END STARTING STATS PANEL
