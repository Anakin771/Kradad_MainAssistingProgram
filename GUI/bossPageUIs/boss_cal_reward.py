"""
***********************************************

Author: MontyGUI

Description:
This script extends bossPage.py and is a child section of boss_generate_boss.py,
it includes the layout and functions of the interface
that calculate Rewards from the generated boss fight.

***********************************************
"""

from tkinter import ttk, messagebox

from bossStat import *


class RewardCalculationUI:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Container Label Frame
        self.container = ttk.LabelFrame(self.frame, text="Rewards")
        self.container.pack(expand=1, fill="both")

        # Generic Text When Generated Boss is None
        self.placeholder = ttk.Label(self.container, text="Boss reward calculation will be shown here.")
        self.placeholder.grid(column=0, row=0, padx=30, pady=40)

        # Money Line
        # Frame
        self.money_frame = ttk.Frame(self.container)
        self.money_frame.grid(column=0, row=1, padx=30)
        # Category Text
        ttk.Label(self.money_frame, text="Money: ", style="category_txt.TLabel")\
            .grid(column=0, row=0, padx=(60, 0), pady=5)
        # Money Text
        self.money_box = ttk.Label(self.money_frame, text="???", style="category_txt.TLabel")
        self.money_box.grid(column=1, row=0, padx=10, pady=5)
        # Coin Unit
        ttk.Label(self.money_frame, text="(C)", style="category_txt.TLabel").grid(column=2, row=0, padx=(0, 60), pady=5)

        # XP Line
        # Frame
        self.xp_frame = ttk.Frame(self.container)
        self.xp_frame.grid(column=0, row=2, padx=30)
        # Category Text
        ttk.Label(self.xp_frame, text="EXP: ", style="category_txt.TLabel")\
            .grid(column=0, row=0, padx=(60, 0), pady=5)
        # XP Text
        self.xp_box = ttk.Label(self.xp_frame, text="???", style="category_txt.TLabel")
        self.xp_box.grid(column=1, row=0, padx=10, pady=5)
        # XP Unit
        ttk.Label(self.xp_frame, text="XP", style="category_txt.TLabel").grid(column=2, row=0, padx=(0, 60), pady=5)

        # Drop Line
        # Frame
        self.drop_frame = ttk.Frame(self.container)
        self.drop_frame.grid(column=0, row=3, padx=30)
        # Category Text
        ttk.Label(self.drop_frame, text="Drop: ", style="category_txt.TLabel")\
            .grid(column=0, row=0, padx=(60, 0), pady=5)
        # Drop Amount Tet
        self.drop_amount_box = ttk.Label(self.drop_frame, text="???", style="category_txt.TLabel")
        self.drop_amount_box.grid(column=1, row=0, padx=10, pady=5)
        # Item Unit
        ttk.Label(self.drop_frame, text="Item(s)", style="category_txt.TLabel")\
            .grid(column=2, row=0, padx=(0, 60), pady=5)

        # Hide reward categories upon initialize
        self.hide_reward()

    def hide_reward(self):
        self.money_frame.grid_forget()
        self.xp_frame.grid_forget()
        self.drop_frame.grid_forget()

        self.placeholder.grid(padx=30, pady=40)

    def show_reward(self):
        self.placeholder.grid_forget()

        self.money_frame.grid(column=0, row=1)
        self.xp_frame.grid(column=0, row=2)
        self.drop_frame.grid(column=0, row=3)

    def display(self, xp, money, item):
        self.show_reward()
        self.xp_box['text'] = str(xp)
        self.money_box['text'] = str(money)
        self.drop_amount_box['text'] = str(item)

    def calculate(self, boss, pal):
        if type(boss) is dict:
            boss_lv = boss["LV"]
            diff = boss["DIFFICULTY"]
        elif type(boss) is list:
            sample_boss = boss[0]
            boss_lv = sample_boss["LV"]
            diff = sample_boss["DIFFICULTY"]
        else:
            messagebox.showerror(title="Error", message="An error has occurred due to faulty coding in bossStat.py\n"
                                                        " Please contact the Developer to report this error.")
            return False
        xp_r, money_r, item_r = calculate_reward(boss_lv, pal, diff)
        self.display(xp_r, money_r, item_r)

    # TODO: Create Method(s) that receives and display calculated reward
