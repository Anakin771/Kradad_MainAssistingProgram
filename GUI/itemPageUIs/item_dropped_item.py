"""
***********************************************

Author: MontyGUI

Description
This script extends itemPage.py,
it includes the layout and functions of the interface
that generates a dropped item from a boss.

***********************************************
"""

import tkinter as tk
from tkinter import ttk

from GUI.itemPageUIs.item_dropped_input import DroppedInputUI


class DroppedItemUI:
    def __init__(self, parent, frame):
        self.parent = parent
        self.frame = frame

        # Heading
        # Head Layer
        self.heading_frame = ttk.Frame(self.frame)
        self.heading_frame.pack(expand=True, fill="both")

        ttk.Label(self.heading_frame, text="Generate Dropped Item", style="tab_header.TLabel")\
            .grid(column=0, row=0)
        ttk.Label(self.heading_frame, text="Get your loot!", style="tab_subtitle.TLabel")\
            .grid(column=1, row=0, sticky="s", padx=10, pady=5)

        # Content Section
        self.content_frame = ttk.Frame(self.frame)
        self.content_frame.pack(expand=True, fill="both")

        # Input Section
        self.input_frame = ttk.Frame(self.content_frame)
        self.input_frame.grid(column=0, row=0)
        self.input = DroppedInputUI(self.content_frame, self.input_frame)

        # Vertical Separator

        # Item Display Section
