"""
***********************************************

Author: MontyGUI

Description:
This script extends bossPage.py and is a child section of boss_generate_boss.py,
it includes the layout and functions of the interface
that calculate Rewards from the generated boss fight.

***********************************************
"""
import tkinter as tk
from tkinter import ttk


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
        self.money_frame.grid(column=0, row=1)
        # Category Text
        ttk.Label(self.money_frame, text="Money: ").grid(column=0, row=0)
        # Money Text
        self.money_box = ttk.Label(self.money_frame, text="???")
        self.money_box.grid(column=1, row=0)
        # Coin Unit
        ttk.Label(self.money_frame, text="(C)").grid(column=2, row=0)

        # XP Line
        # Frame
        self.xp_frame = ttk.Frame(self.container)
        self.xp_frame.grid(column=0, row=2)
        # Category Text
        ttk.Label(self.xp_frame, text="EXP: ").grid(column=0, row=0)
        # XP Text
        self.xp_box = ttk.Label(self.xp_frame, text="???")
        self.xp_box.grid(column=1, row=0)
        # XP Unit
        ttk.Label(self.xp_frame, text="XP").grid(column=2, row=0)

        # Drop Line
        # Frame
        self.drop_frame = ttk.Frame(self.container)
        self.drop_frame.grid(column=0, row=3)
        # Category Text
        ttk.Label(self.drop_frame, text="Drop: ").grid(column=0, row=0)
        # Drop Amount Tet
        self.drop_amount_box = ttk.Label(self.drop_frame, text="???")
        self.drop_amount_box.grid(column=1, row=0)
        # Item Unit
        ttk.Label(self.drop_frame, text="Item(s)").grid(column=2, row=0)

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

    # TODO: Create Method(s) that receives and display calculated reward
