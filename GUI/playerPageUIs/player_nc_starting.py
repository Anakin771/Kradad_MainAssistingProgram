"""
***********************************************

Author: MontyGUI

Description
This script extends playerPage.py and is a child section of player_new_char.py,
it includes the layout and functions of the interface
that generates starting stats of a new character.

***********************************************
"""
import random
import tkinter as tk
from tkinter import ttk

from playerStat import random_char_stat_single, STARTING_BASE_ROLL, STARTING_MTP

JIGGLE_LIMIT = 25


class StartingStatsUI:
    def __init__(self, parent, frame, bnrp_ui=None):
        self.parent = parent
        self.frame = frame
        self.bnrp_ui = bnrp_ui
        self.jiggle = 0
        self.animation = None
        self.blank = True

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
        self.strts_hp_box = ttk.Label(
            self.strts_display_panel,
            width=6,
            relief="sunken",
            style="strts_stat.TLabel",
            anchor="center"
        )
        self.strts_hp_box.configure(background="white")

        # P. ATK Box
        self.strts_patk_box = ttk.Label(
            self.strts_display_panel,
            width=6,
            relief="sunken",
            style="strts_stat.TLabel",
            anchor="center"
        )
        self.strts_patk_box.configure(background="white")

        # M. ATK Box
        self.strts_matk_box = ttk.Label(
            self.strts_display_panel,
            width=6,
            relief="sunken",
            style="strts_stat.TLabel",
            anchor="center"
        )
        self.strts_matk_box.configure(background="white")

        # P. DEF Box
        self.strts_pdef_box = ttk.Label(
            self.strts_display_panel,
            width=6,
            relief="sunken",
            style="strts_stat.TLabel",
            anchor="center"
        )
        self.strts_pdef_box.configure(background="white")

        # M. DEF Box
        self.strts_mdef_box = ttk.Label(
            self.strts_display_panel,
            width=6,
            relief="sunken",
            style="strts_stat.TLabel",
            anchor="center"
        )
        self.strts_mdef_box.configure(background="white")

        # FREE Box
        self.strts_free_box = ttk.Label(
            self.strts_display_panel,
            width=6,
            relief="sunken",
            style="strts_stat.TLabel",
            anchor="center"
        )
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
        self.random_btn = ttk.Button(self.strts_buttons_frame, text="Random",
                                     command=lambda: self.random_animation(lambda: self.random_stat()))
        self.random_btn.grid(column=0, row=0, pady=10, ipady=5)
        self.confirm_btn = ttk.Button(self.strts_buttons_frame, text="Confirm", command=lambda: self.confirm_panel())
        self.confirm_btn.grid(column=0, row=2, pady=10, ipady=5)

        # END STARTING STATS PANEL

        self.enable_panel()

    def random_stat(self):
        sample_strts = random_char_stat_single(STARTING_BASE_ROLL, STARTING_MTP, show_stat=False)
        self.strts_hp_box['text'] = sample_strts["HP"]
        self.strts_patk_box['text'] = sample_strts["PATK"]
        self.strts_matk_box['text'] = sample_strts["MATK"]
        self.strts_pdef_box['text'] = sample_strts["PDEF"]
        self.strts_mdef_box['text'] = sample_strts["MDEF"]
        self.strts_free_box['text'] = sample_strts["FREE"]
        self.confirm_btn.configure(state="enabled")

    def disable_panel(self):
        self.strts_hp_box.configure(background="#aaaaaa")
        self.strts_patk_box.configure(background="#aaaaaa")
        self.strts_matk_box.configure(background="#aaaaaa")
        self.strts_pdef_box.configure(background="#aaaaaa")
        self.strts_mdef_box.configure(background="#aaaaaa")
        self.strts_free_box.configure(background="#aaaaaa")
        self.random_btn.configure(state="disabled")
        self.confirm_btn.configure(state="disabled")

    def enable_panel(self):
        self.strts_hp_box.configure(background="white")
        self.strts_patk_box.configure(background="white")
        self.strts_matk_box.configure(background="white")
        self.strts_pdef_box.configure(background="white")
        self.strts_mdef_box.configure(background="white")
        self.strts_free_box.configure(background="white")
        self.random_btn.configure(state="enabled")
        if self.blank:
            self.confirm_btn.configure(state="disabled")
        else:
            self.confirm_btn.configure(state="enabled")

    def confirm_panel(self):
        self.strts_hp_box.configure(background="#ccffcc")
        self.strts_patk_box.configure(background="#ccffcc")
        self.strts_matk_box.configure(background="#ccffcc")
        self.strts_pdef_box.configure(background="#ccffcc")
        self.strts_mdef_box.configure(background="#ccffcc")
        self.strts_free_box.configure(background="#ccffcc")
        self.random_btn.configure(state="disabled")
        self.confirm_btn.configure(state="disabled")
        self.bnrp_ui.enable_panel()

    def random_animation(self, callback):
        if self.jiggle >= JIGGLE_LIMIT:
            self.strts_display_panel.after_cancel(self.animation)
            self.animation = None
            self.jiggle = 0
            callback()
        else:
            num1, num2, num3, num4, num5, num6 = random.sample(range(1, 101), 6)
            self.strts_hp_box['text'] = str(num1)
            self.strts_patk_box['text'] = str(num2)
            self.strts_matk_box['text'] = str(num3)
            self.strts_pdef_box['text'] = str(num4)
            self.strts_mdef_box['text'] = str(num5)
            self.strts_free_box['text'] = str(num6)
            self.jiggle += 1
            self.confirm_btn.configure(state="disabled")
            self.animation = self.strts_display_panel.after(50, lambda: self.random_animation(callback))

    def clear(self):
        self.strts_hp_box['text'] = ""
        self.strts_patk_box['text'] = ""
        self.strts_matk_box['text'] = ""
        self.strts_pdef_box['text'] = ""
        self.strts_mdef_box['text'] = ""
        self.strts_free_box['text'] = ""
        self.blank = True
