"""
***********************************************

Author: MontyGUI

Description:
This script includes the GUI of the Item Page,
which includes the functionality like the itemStat.py
scripts found within this project, but operates in a GUI fashion

***********************************************
"""

import tkinter as tk
from tkinter import ttk, messagebox
from GUI.itemPageUIs.item_dropped_item import DroppedItemUI


class ItemPage:
    def __init__(self, parent, frame):
        self.parent = parent
        self.frame = frame

        # Container
        self.container = ttk.Frame(self.frame, relief="groove", borderwidth=3)
        self.container.pack(padx=10, pady=10, ipadx=10, ipady=10)

        # Dropped Item Box
        # Dropped Item Frame
        self.dropped_item_frame = ttk.Frame(self.container)
        self.dropped_item_frame.pack()
        self.dropped_item = DroppedItemUI(self.container, self.dropped_item_frame)

        # Actions Separator
        ttk.Separator(self.container).pack(expand=True, fill="x", padx=20)

        # Craft Item Box
