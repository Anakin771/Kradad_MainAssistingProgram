"""
***********************************************

Author: MontyGUI

Description:
This script extends bossPage.py and is a child section of boss_generate_boss.py,
it includes the layout and functions of the interface
that displays all bosses that have been generated

***********************************************
"""
import random
from tkinter import ttk

# Non Built-in imports:
from Externals.multiColumn import MultiColumnListbox

JIGGLE_LIMIT = 25


class BossDisplayUI:
    def __init__(self, root, frame, version, input_ui=None):
        self.root = root
        self.frame = frame
        self.VERSION = version
        self.input_ui = input_ui

        self.jiggle = 0
        self.animation = None

        # Widget Controls

        # Placeholder Label
        self.placeholder_lbl = ttk.Label(
            self.frame,
            text="Generated Boss Stats will be shown here.",
            style="placeholder.TLabel"
        )
        self.placeholder_lbl.pack(ipady=140)

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

        # Multi-Boss Table
        self.multi_boss_frame = ttk.Frame(self.frame)
        self.multi_boss_frame.pack(expand=True, fill="both")

        boss_header = ["Boss", "LV", "HP", "P. ATK", "M.ATK", "P. DEF", 'M. DEF']
        boss_datatype = [0, 1, 1, 1, 1, 1, 1]

        ttk.Label(self.multi_boss_frame, text="-------- MULTI-BOSS FIGHT --------", style="multi_header.TLabel") \
            .pack(pady=(0, 10))

        self.multi_table_frame = ttk.Frame(self.multi_boss_frame)
        self.multi_table_frame.pack(expand=True, fill="both")

        self.multi_boss_table = MultiColumnListbox(
            self.multi_table_frame,
            self.multi_table_frame,
            boss_header,
            boss_datatype,
            [],
            heading_txt="MULTI-BOSS FIGHT",
            table_style="multi_display"
        )

        self.show_placeholder()

    def show_placeholder(self):
        self.placeholder_lbl.pack(expand=True)
        self.single_boss_frame.pack_forget()
        self.multi_boss_frame.pack_forget()

    def show_single_boss(self):
        self.placeholder_lbl.pack_forget()
        self.single_boss_frame.pack(expand=True, fill="both", padx=25, pady=25)
        self.multi_boss_frame.pack_forget()

    def show_multi_boss(self):
        self.placeholder_lbl.pack_forget()
        self.single_boss_frame.pack_forget()
        self.multi_boss_frame.pack(expand=True, fill="both", pady=20)

    def display(self, boss):
        # Check for Single Boss, which is in dictionary type
        if type(boss) is dict:
            self.animate_single(lambda: self.display_single(boss))
        elif type(boss) is list:
            self.input_ui.generate_btn.configure(state="disabled")
            self.display_multiple(boss)
            self.animation = self.single_stats_frame.after(
                1500,
                lambda: self.input_ui.generate_btn.configure(state="enabled")
            )

    def display_single(self, boss_dict):
        self.show_single_boss()
        self.diff_lv_box['text'] = f"{boss_dict['DIFFICULTY'].upper()} DIFFICULTY - LV. {boss_dict['LV']}"
        self.single_hp['text'] = str(boss_dict['HP'])
        self.single_patk['text'] = str(boss_dict['PATK'])
        self.single_matk['text'] = str(boss_dict['MATK'])
        self.single_pdef['text'] = str(int(boss_dict['PDEF'] / 2))
        self.single_mdef['text'] = str(int(boss_dict['MDEF'] / 2))

    def display_multiple(self, boss_list):
        self.show_multi_boss()
        boss_info_table = []
        count = 0
        for boss_row in boss_list:
            current_row = [
                f"Boss #{count + 1}",
                boss_row['LV'],
                boss_row['HP'],
                boss_row['PATK'],
                boss_row['MATK'],
                int(boss_row['PDEF'] / 2),
                int(boss_row['MDEF'] / 2)
            ]
            boss_info_table.append(current_row)
            count += 1
        self.multi_boss_table.update_list(boss_info_table)

    def animate_single(self, callback):
        if self.jiggle == 0:
            self.show_single_boss()
            callback()

        if self.jiggle >= JIGGLE_LIMIT:
            self.single_stats_frame.after_cancel(self.animation)
            self.animation = None
            self.jiggle = 0
            self.input_ui.generate_btn.configure(state="enabled")
            callback()
        else:
            num1, num2, num3, num4 = random.sample(range(1, 2001), 4)
            self.single_patk['text'] = str(num1)
            self.single_matk['text'] = str(num2)
            self.single_pdef['text'] = str(num3)
            self.single_mdef['text'] = str(num4)
            self.jiggle += 1
            self.input_ui.generate_btn.configure(state="disabled")
            self.animation = self.single_stats_frame.after(50, lambda: self.animate_single(callback))
