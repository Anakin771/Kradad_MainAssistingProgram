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
import random
from tkinter import ttk

from playerStat import random_char_stat_single, BONUS_BASE_ROLL, BONUS_MTP

JIGGLE_LIMIT = 25


class BonusRateUI:
    def __init__(self, parent, frame, version, action_ui=None):
        self.parent = parent
        self.frame = frame
        self.VERSION = version
        self.action_ui = action_ui
        self.jiggle = 0
        self.animation = None
        self.blank = True

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
        self.bnrp_hp_box = ttk.Label(
            self.bnrp_display_panel,
            width=6,
            relief="sunken",
            style="bnrp_stat.TLabel",
            anchor="center"
        )
        self.bnrp_hp_box.configure(background="white")

        # P. ATK Box
        self.bnrp_patk_box = ttk.Label(
            self.bnrp_display_panel,
            width=6,
            relief="sunken",
            style="bnrp_stat.TLabel",
            anchor="center"
        )
        self.bnrp_patk_box.configure(background="white")

        # M. ATK Box
        self.bnrp_matk_box = ttk.Label(
            self.bnrp_display_panel,
            width=6,
            relief="sunken",
            style="bnrp_stat.TLabel",
            anchor="center"
        )
        self.bnrp_matk_box.configure(background="white")

        # P. DEF Box
        self.bnrp_pdef_box = ttk.Label(
            self.bnrp_display_panel,
            width=6,
            relief="sunken",
            style="bnrp_stat.TLabel",
            anchor="center"
        )
        self.bnrp_pdef_box.configure(background="white")

        # M. DEF Box
        self.bnrp_mdef_box = ttk.Label(
            self.bnrp_display_panel,
            width=6,
            relief="sunken",
            style="bnrp_stat.TLabel",
            anchor="center"
        )
        self.bnrp_mdef_box.configure(background="white")

        # FREE Box
        self.bnrp_free_box = ttk.Label(
            self.bnrp_display_panel,
            width=6,
            relief="sunken",
            style="bnrp_stat.TLabel",
            anchor="center"
        )
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
        self.random_btn = ttk.Button(
            self.bnrp_buttons_frame,
            text="Random",
            command=lambda: self.random_animation(lambda: self.random_stat())
        )
        self.random_btn.grid(column=0, row=0, pady=5, ipady=5)
        self.confirm_btn = ttk.Button(
            self.bnrp_buttons_frame,
            text="Confirm",
            command=lambda: self.confirm_panel()
        )
        self.confirm_btn.grid(column=0, row=1, pady=5, ipady=5)

        self.try_again_btn = ttk.Button(
            self.bnrp_buttons_frame,
            text="Try Again",
            state="disabled",
            command=lambda: self.action_ui.restart_random()
        )
        self.try_again_btn.grid(column=0, row=2, pady=5, ipady=5)

        # END STARTING STATS PANEL

        self.disable_panel()

    def disable_panel(self):
        self.bnrp_hp_box.configure(background="#aaaaaa")
        self.bnrp_patk_box.configure(background="#aaaaaa")
        self.bnrp_matk_box.configure(background="#aaaaaa")
        self.bnrp_pdef_box.configure(background="#aaaaaa")
        self.bnrp_mdef_box.configure(background="#aaaaaa")
        self.bnrp_free_box.configure(background="#aaaaaa")
        self.random_btn.configure(state="disabled")
        self.confirm_btn.configure(state="disabled")
        self.try_again_btn.configure(state="disabled")

    def enable_panel(self):
        self.bnrp_hp_box.configure(background="white")
        self.bnrp_patk_box.configure(background="white")
        self.bnrp_matk_box.configure(background="white")
        self.bnrp_pdef_box.configure(background="white")
        self.bnrp_mdef_box.configure(background="white")
        self.bnrp_free_box.configure(background="white")
        self.random_btn.configure(state="enabled")
        self.try_again_btn.configure(state="disabled")
        if self.blank:
            self.confirm_btn.configure(state="disabled")
        else:
            self.confirm_btn.configure(state="enabled")

    def confirm_panel(self):
        self.bnrp_hp_box.configure(background="#ccffcc")
        self.bnrp_patk_box.configure(background="#ccffcc")
        self.bnrp_matk_box.configure(background="#ccffcc")
        self.bnrp_pdef_box.configure(background="#ccffcc")
        self.bnrp_mdef_box.configure(background="#ccffcc")
        self.bnrp_free_box.configure(background="#ccffcc")
        self.random_btn.configure(state="disabled")
        self.confirm_btn.configure(state="disabled")
        self.try_again_btn.configure(state="enabled")

    def random_stat(self):
        sample_bnrp = random_char_stat_single(BONUS_BASE_ROLL, BONUS_MTP, show_stat=False)
        self.bnrp_hp_box['text'] = sample_bnrp["HP"]
        self.bnrp_patk_box['text'] = sample_bnrp["PATK"]
        self.bnrp_matk_box['text'] = sample_bnrp["MATK"]
        self.bnrp_pdef_box['text'] = sample_bnrp["PDEF"]
        self.bnrp_mdef_box['text'] = sample_bnrp["MDEF"]
        self.bnrp_free_box['text'] = sample_bnrp["FREE"]
        self.confirm_btn.configure(state="enabled")
        
    def random_animation(self, callback):
        if self.jiggle >= JIGGLE_LIMIT:
            self.bnrp_display_panel.after_cancel(self.animation)
            self.animation = None
            self.jiggle = 0
            callback()
        else:
            num1, num2, num3, num4, num5, num6 = random.sample(range(1, 101), 6)
            self.bnrp_hp_box['text'] = str(num1)
            self.bnrp_patk_box['text'] = str(num2)
            self.bnrp_matk_box['text'] = str(num3)
            self.bnrp_pdef_box['text'] = str(num4)
            self.bnrp_mdef_box['text'] = str(num5)
            self.bnrp_free_box['text'] = str(num6)
            self.jiggle += 1
            self.confirm_btn.configure(state="disabled")
            self.animation = self.bnrp_display_panel.after(50, lambda: self.random_animation(callback))
            
    def clear(self):
        self.bnrp_hp_box['text'] = ""
        self.bnrp_patk_box['text'] = ""
        self.bnrp_matk_box['text'] = ""
        self.bnrp_pdef_box['text'] = ""
        self.bnrp_mdef_box['text'] = ""
        self.bnrp_free_box['text'] = ""
        self.blank = True
