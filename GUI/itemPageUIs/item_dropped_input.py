"""
***********************************************

Author: MontyGUI

Description:
This script extends itemPage.py and is a child section of item_dropped_item.py,
it includes the layout and functions of the interface
that inputs information necessary to generate boss dropped item

***********************************************
"""

import sys
import tkinter as tk
from tkinter import ttk


class DroppedInputUI:
    def __init__(self, parent, frame):
        self.parent = parent
        self.frame = frame

        # Boss LV
        # Label
        ttk.Label(self.frame, text="Boss LV: ", style="category_txt.TLabel")\
            .grid(column=0, row=0)
        # Spinbox
        self.boss_lv_init = tk.StringVar(self.frame)
        self.boss_lv_init.set("1")
        self.boss_lv_box = ttk.Spinbox(
            self.frame,
            from_=1,
            to=sys.maxsize,
            textvariable=self.boss_lv_init
        )
        self.boss_lv_box.grid(column=1, row=0)

        # Item Type
        ttk.Label(self.frame, text="Item Type: ", style="category_txt.TLabel") \
            .grid(column=0, row=1)

        # Item Type

        # Clear Button

        # Calculate Button

        # Styling
        self.boss_lv_box.configure(font=("Helvetica", 11, "bold"))
