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
from playerStat import cal_req_xp


class LevelUpDisplayUI:
    def __init__(self, root, frame, version, lu_input=None):
        self.root = root
        self.frame = frame
        self.VERSION = version
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
        )
        self.rem_xp_txt.grid(column=0, columnspan=4, row=2, pady=5)

        # Display Line: To Next LV
        self.to_next = ttk.Label(self.summary_frame, text="To next LV: ", style="lu_category.TLabel")
        self.to_next.grid(column=0, columnspan=4, row=3, pady=5)

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

    def show_lvl_up(self):
        self.summary_frame.grid(column=0, row=1)
        self.show_new_level_line()
        self.rem_xp_txt.grid(column=0, columnspan=4, row=2, pady=5)
        self.to_next.grid(column=0, columnspan=4, row=3, pady=5)

    def hide_lvl_up(self):
        self.summary_frame.grid_forget()
        self.hide_new_level_line()
        self.rem_xp_txt.grid_forget()
        self.to_next.grid_forget()

    def show_xp_progress(self):
        self.summary_frame.grid(column=0, row=1)
        self.rem_xp_txt.grid(column=0, columnspan=4, row=2, pady=5)
        self.to_next.grid(column=0, columnspan=4, row=3, pady=5)

    def hide_xp_progress(self):
        self.summary_frame.grid_forget()
        self.rem_xp_txt.grid_forget()
        self.to_next.grid_forget()

    def show_skl_up(self):
        self.sp_gained_box.grid(column=0, columnspan=4, row=4, pady=5)

    def hide_skl_up(self):
        self.sp_gained_box.grid_forget()

    def hide_footnote(self):
        self.fallen_penalty_txt.grid_forget()
        self.double_xp_txt.grid_forget()
        self.itm_decl_bonus_txt.grid_forget()

    def reset_display(self):
        self.lvl_up_msg_box['text'] = f"The result of your character's\nLV Calculation will be shown here."
        self.summary_frame.grid_forget()
        self.hide_skl_up()
        self.hide_new_level_line()
        self.rem_xp_txt.grid_forget()
        self.to_next.grid_forget()
        self.hide_footnote()

    def display(self, lvl_progress):
        # Reset Display for new calculations
        self.reset_display()

        if lvl_progress['old']['lv'] <= 10:
            self.double_xp_txt.grid(column=0, row=2, sticky="w")

        if lvl_progress["fallen_penalty"] > 0:
            self.fallen_penalty_txt.grid(column=0, row=1, sticky="w")
            self.fallen_penalty_txt['text'] = \
                f" * {lvl_progress['fallen']} Party member(s) have fallen:" \
                f"-{lvl_progress['fallen_penalty']}% XP Penalty"

        if lvl_progress['item_decl']:
            self.itm_decl_bonus_txt.grid(column=0, row=3, sticky="w")

        if not lvl_progress["lv_up"]:
            # Level is not changed
            self.lvl_up_msg_box['text'] = f"You did not level up...\n {lvl_progress['note']}"
            if lvl_progress["gained_xp"] > 0:
                # Gain XP, but did not level up
                self.show_xp_progress()
                self.rem_xp_txt['text'] = \
                    f"Remainder XP: {lvl_progress['old']['rem_xp']} ➞ {lvl_progress['new']['rem_xp']}"
                self.to_next['text'] = f"To Next LV: {cal_req_xp(lvl_progress['new']['lv'])}"
            else:
                # Gained 0 EXP
                self.show_xp_progress()
                self.rem_xp_txt['text'] = \
                    f"Remainder XP: {lvl_progress['new']['rem_xp']} (+0)"
                self.to_next['text'] = f"To Next LV: {cal_req_xp(lvl_progress['new']['lv'])}"
        else:
            # Level Up
            self.lvl_up_msg_box['text'] = f"You leveled up!"
            self.show_lvl_up()
            self.old_lv_box['text'] = str(lvl_progress['old']['lv'])
            self.new_lv_box['text'] = str(lvl_progress['new']['lv'])
            self.rem_xp_txt['text'] = \
                f"Remainder XP: {lvl_progress['old']['rem_xp']} ➞ {lvl_progress['new']['rem_xp']}"
            self.to_next['text'] = f"To Next LV: {cal_req_xp(lvl_progress['new']['lv'])}"
            if 0 < lvl_progress['gained_sp'] == 1:
                # Gained 1 Skill Point
                self.show_skl_up()
                self.sp_gained_box['text'] = f"+{lvl_progress['gained_sp']} Skill Point"
            elif lvl_progress['gained_sp'] > 1:
                # Gained Skill Points
                self.show_skl_up()
                self.sp_gained_box['text'] = f"+{lvl_progress['gained_sp']} Skill Points"
            else:
                # Gained no Skill Points
                self.hide_skl_up()
