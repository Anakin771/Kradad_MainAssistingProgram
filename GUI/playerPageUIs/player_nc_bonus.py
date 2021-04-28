"""
***********************************************

Author: MontyGUI

Description
This script extends playerPage.py and is a child section of player_new_char.py,
it includes the layout and functions of the interface
that generates bonus rate of a new character.
***********************************************
"""

import tkinter as tk
from tkinter import ttk


class BonusRateUI:
    def __init__(self, parent, frame, strts_ui=None):
        self.parent = parent
        self.frame = frame
        self.strts_ui = strts_ui

        # Starting Stats - Heading Text
        ttk.Label(
            self.frame,
            text="Step 2 - Generating Bonus Rate Points",
            style="bnrp_text.TLabel"
        ) \
            .grid(column=0, row=0, columnspan=2, pady=10)

        # Starting Stats - Stats Panel
        self.bnrp_display_panel = ttk.Frame(self.frame)
        self.bnrp_display_panel.grid(column=0, row=1)

        # Starting Stats - Stats Display
        # Stats Name Label
        ttk.Label(self.bnrp_display_panel, text="HP: ", style="bnrp_stat.TLabel").grid(column=0, row=0)
        ttk.Label(self.bnrp_display_panel, text="P. ATK: ", style="bnrp_stat.TLabel").grid(column=0, row=1)
        ttk.Label(self.bnrp_display_panel, text="M. ATK: ", style="bnrp_stat.TLabel").grid(column=0, row=2)
        ttk.Label(self.bnrp_display_panel, text="P. DEF: ", style="bnrp_stat.TLabel").grid(column=0, row=3)
        ttk.Label(self.bnrp_display_panel, text="M. DEF: ", style="bnrp_stat.TLabel").grid(column=0, row=4)
        ttk.Label(self.bnrp_display_panel, text="FREE: ", style="bnrp_stat.TLabel").grid(column=0, row=5)

        # Stats Number Boxes
        # HP Box
        self.bnrp_hp_box = ttk.Label(self.bnrp_display_panel, width=6, relief="sunken")
        self.bnrp_hp_box.configure(background="white")

        # P. ATK Box
        self.bnrp_patk_box = ttk.Label(self.bnrp_display_panel, width=6, relief="sunken")
        self.bnrp_patk_box.configure(background="white")

        # M. ATK Box
        self.bnrp_matk_box = ttk.Label(self.bnrp_display_panel, width=6, relief="sunken")
        self.bnrp_matk_box.configure(background="white")

        # P. DEF Box
        self.bnrp_pdef_box = ttk.Label(self.bnrp_display_panel, width=6, relief="sunken")
        self.bnrp_pdef_box.configure(background="white")

        # M. DEF Box
        self.bnrp_mdef_box = ttk.Label(self.bnrp_display_panel, width=6, relief="sunken")
        self.bnrp_mdef_box.configure(background="white")

        # FREE Box
        self.bnrp_free_box = ttk.Label(self.bnrp_display_panel, width=6, relief="sunken")
        self.bnrp_free_box.configure(background="white")

        # Alignment
        self.bnrp_hp_box.grid(column=1, row=0, padx=5)
        self.bnrp_patk_box.grid(column=1, row=1, padx=5)
        self.bnrp_matk_box.grid(column=1, row=2, padx=5)
        self.bnrp_pdef_box.grid(column=1, row=3, padx=5)
        self.bnrp_mdef_box.grid(column=1, row=4, padx=5)
        self.bnrp_free_box.grid(column=1, row=5, padx=5)

        # Unit Ending (pts.)
        ttk.Label(self.bnrp_display_panel, text=" pts.", style="bnrp_stat.TLabel").grid(column=2, row=0)
        ttk.Label(self.bnrp_display_panel, text=" pts.", style="bnrp_stat.TLabel").grid(column=2, row=1)
        ttk.Label(self.bnrp_display_panel, text=" pts.", style="bnrp_stat.TLabel").grid(column=2, row=2)
        ttk.Label(self.bnrp_display_panel, text=" pts.", style="bnrp_stat.TLabel").grid(column=2, row=3)
        ttk.Label(self.bnrp_display_panel, text=" pts.", style="bnrp_stat.TLabel").grid(column=2, row=4)
        ttk.Label(self.bnrp_display_panel, text=" pts.", style="bnrp_stat.TLabel").grid(column=2, row=5)

        # END: Starting Stats - Stats Panel

        # Starting Stats - Action Buttons Panel
        self.bnrp_buttons_frame = ttk.Frame(self.frame)
        self.bnrp_buttons_frame.grid(column=1, row=1)

        # Starting Stat - Random Button
        # TODO: Insert Random (and Re-Random) command into Random Button
        ttk.Button(self.bnrp_buttons_frame, text="Random").grid(column=0, row=0, pady=10, ipady=5)
        # TODO: Insert Stat-Locking command into Confirm Button
        ttk.Button(self.bnrp_buttons_frame, text="Confirm").grid(column=0, row=2, pady=10, ipady=5)

        # END STARTING STATS PANEL
