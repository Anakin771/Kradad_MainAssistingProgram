"""
***********************************************

Author: MontyGUI

Description:
This script extends bossPage.py and is a child section of boss_generate_boss.py,
it includes the layout and functions of the interface
that displays all bosses that have been generated

***********************************************
"""
import tkinter as tk
from tkinter import ttk


class BossDisplayUI:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Widget Controls

        # Placeholder Label
        self.placeholder_lbl = ttk.Label(
            self.frame,
            text="Generated Boss Stats will be shown here.",
            style="placeholder.TLabel"
        )
        self.placeholder_lbl.pack(expand=True)

        # TODO: Tomorrow - Creates Single-Boss UI and Multi-Boss UI (and make sure it's proper)

        # Single Boss Frame
        self.single_boss_frame = ttk.Frame(self.frame, relief="groove", borderwidth=3)
        self.single_boss_frame.pack(expand=True, fill="both", padx=25, pady=25)

        # Boss Header Line
        self.single_header = ttk.Label(
            self.single_boss_frame,
            text="-------- BOSS --------",
            style="single_boss_header.TLabel"
        )
        self.single_header.pack()

        # Boss Difficulty & LV
        self.diff_lv_box = ttk.Label(
            self.single_boss_frame,
            text="[Diff] DIFFICULTY - LV. [lvl]",
            style="single_boss_subheader.TLabel"
        )
        self.diff_lv_box.pack()

        # Stats Frame
        self.single_stats_frame = ttk.Frame(self.single_boss_frame)
        self.single_stats_frame.pack(padx=20, pady=20)

        # HP Line
        ttk.Label(
            self.single_stats_frame,
            text="HP: ",
            style="single_boss_stat.TLabel"
        ).grid(column=0, row=0)
        self.single_hp = ttk.Label(self.single_stats_frame, text="???", style="single_boss_stat.TLabel")
        self.single_hp.grid(column=1, row=0)

        # P. ATK Line
        ttk.Label(
            self.single_stats_frame,
            text="P. ATK: ",
            style="single_boss_stat.TLabel"
        ).grid(column=0, row=1)
        self.single_patk = ttk.Label(self.single_stats_frame, text="???", style="single_boss_stat.TLabel")
        self.single_patk.grid(column=1, row=1)

        # M. ATK Line
        ttk.Label(
            self.single_stats_frame,
            text="M. ATK: ",
            style="single_boss_stat.TLabel"
        ).grid(column=0, row=2)
        self.single_matk = ttk.Label(self.single_stats_frame, text="???", style="single_boss_stat.TLabel")
        self.single_matk.grid(column=1, row=2)

        # P. DEF Line
        ttk.Label(
            self.single_stats_frame,
            text="P. DEF: ",
            style="single_boss_stat.TLabel"
        ).grid(column=0, row=3)
        self.single_pdef = ttk.Label(self.single_stats_frame, text="???", style="single_boss_stat.TLabel")
        self.single_pdef.grid(column=1, row=3)

        # M. DEF Line
        ttk.Label(
            self.single_stats_frame,
            text="MDEF: ",
            style="single_boss_stat.TLabel"
        ).grid(column=0, row=4)
        self.single_mdef = ttk.Label(self.single_stats_frame, text="???", style="single_boss_stat.TLabel")
        self.single_mdef.grid(column=1, row=4)
