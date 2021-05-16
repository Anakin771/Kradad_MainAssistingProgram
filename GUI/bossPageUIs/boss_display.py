"""
***********************************************

Author: MontyGUI

Description:
This script extends bossPage.py and is a child section of boss_generate_boss.py,
it includes the layout and functions of the interface
that displays all bosses that have been generated

***********************************************
"""

from tkinter import ttk

# Non Built-in imports:
from Externals.multiColumn import MultiColumnListbox


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

        ttk.Label(self.multi_boss_frame, text="-------- MULTI-BOSS FIGHT --------", style="multi_header.TLabel")\
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
            self.show_single_boss()
            self.diff_lv_box['text'] = f"{boss['DIFFICULTY'].upper()} DIFFICULTY - LV. {boss['LV']}"
            self.single_hp['text'] = str(boss['HP'])
            self.single_patk['text'] = str(boss['PATK'])
            self.single_matk['text'] = str(boss['MATK'])
            self.single_pdef['text'] = str(int(boss['PDEF'] / 2))
            self.single_mdef['text'] = str(int(boss['MDEF'] / 2))
        elif type(boss) is list:
            self.show_multi_boss()
            boss_info_table = []
            count = 0
            for boss_row in boss:
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
