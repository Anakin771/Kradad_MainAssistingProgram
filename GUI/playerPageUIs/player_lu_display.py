"""
***********************************************

Author: MontyGUI

Description
This script extends playerPage.py and is a child section of player_level_up.py,
it includes the layout and functions of the interface
that displays the calculated LV Progress.
***********************************************
"""

import tkinter as tk
from tkinter import ttk, Message

# Non Built-in Imports


class LevelUpDisplayUI:
    def __init__(self, root, frame, lu_input=None):
        self.root = root
        self.frame = frame
        self.lu_input = lu_input

        # Results Label Frame
        self.result_lb_frame = ttk.LabelFrame(self.frame, text="Results")
        self.result_lb_frame.grid(column=0, row=0)

        # Results Label Frame Container
        self.rlbf_container = ttk.Frame(self.result_lb_frame)
        self.rlbf_container.pack(padx=15, pady=10)

        # Level Up Message Box
        self.lvl_up_msg_box = ttk.Label(
            self.rlbf_container,
            text="The result of your character's\nLV Calculation will be shown here.",
            relief="groove",
            borderwidth=2,
            anchor="center",
            style="lu_lv_up_msg.TLabel"
        )
        self.lvl_up_msg_box.grid(column=0, row=0, pady=5, ipadx=25, ipady=10, sticky="we")

        # Summary Text Frame
        self.summary_frame = ttk.Frame(self.rlbf_container)
        self.summary_frame.grid(column=0, row=1)

        # Default: Hide Summary Texts on Start
        self.summary_frame.grid_forget()

        # Display Line: New LV
        # Head
        self.lvl_head = ttk.Label(self.summary_frame, text="Level: ", style="lu_category.TLabel")
        self.lvl_head.grid(column=0, row=1, pady=5)
        # Old LV
        self.old_lv_box = ttk.Label(self.summary_frame, text="Old LV", style="lu_category.TLabel")
        self.old_lv_box.grid(column=1, row=1)
        # Right Arrow
        self.ra = ttk.Label(self.summary_frame, text="➞", style="lu_category.TLabel")
        self.ra.grid(column=2, row=1)
        # New LV
        self.new_lv_box = ttk.Label(self.summary_frame, text="New LV", style="lu_category.TLabel")
        self.new_lv_box.grid(column=3, row=1)

        # Default: Hide New LV Line
        self.hide_new_level_line()

        # Display Line: Remainder XP
        self.rem_xp_txt = ttk.Label(
            self.summary_frame,
            text="Remainder XP: ",
            style="lu_category.TLabel"
        ).grid(column=0, row=2, pady=5)

        # Display Line: To Next LV
        ttk.Label(self.summary_frame, text="To next LV: ", style="lu_category.TLabel").grid(column=0, row=3, pady=5)

        # Display Line: Skill Points
        self.sp_gained_box = ttk.Label(self.summary_frame, text="+N Skill Point(s)", style="lu_category.TLabel")
        self.sp_gained_box.grid(column=0, columnspan=4, row=4, pady=5)
        self.sp_gained_box.grid_forget()

        # END IN RESULTS LABEL FRAME

        # Footnotes
        # -10% XP Penalty Text
        self.fallen_penalty_txt = ttk.Label(
            self.frame,
            text=" * N Party member(s) have fallen: -10N% XP Penalty",
            style="lu_footnote.TLabel"
        )
        self.fallen_penalty_txt.configure(foreground="red")
        self.fallen_penalty_txt.grid(column=0, row=1, sticky="w")
        self.fallen_penalty_txt.grid_forget()

        # LV 1-10 Double XP Bonus Text
        self.double_xp_txt = ttk.Label(
            self.frame,
            text=" * Double XP for LV 10 or lower players",
            style="lu_footnote.TLabel"
        )
        self.double_xp_txt.grid(column=0, row=2, sticky="w")
        self.double_xp_txt.grid_forget()

        # Declining Item 20% XP Bonus Text
        self.itm_decl_bonus_txt = ttk.Label(
            self.frame,
            text=" * Item Declined: +20% XP Bonus",
            style="lu_footnote.TLabel"
        )
        self.itm_decl_bonus_txt.grid(column=0, row=3, sticky="w")
        self.itm_decl_bonus_txt.grid_forget()

    def hide_new_level_line(self):
        self.lvl_head.grid_forget()
        self.old_lv_box.grid_forget()
        self.ra.grid_forget()
        self.new_lv_box.grid_forget()

    def show_new_level_line(self):
        self.lvl_head.grid(column=0, row=1, pady=5)
        self.old_lv_box.grid(column=1, row=1)
        self.ra.grid(column=2, row=1)
        self.new_lv_box.grid(column=3, row=1)
