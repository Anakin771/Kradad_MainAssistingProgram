"""
***********************************************

Author: MontyGUI

Description
This script extends itemPage.py,
it includes the layout and functions of the interface
that generate crafted items

***********************************************
"""

import tkinter as tk
from tkinter import ttk

# Non-builtins
from GUI.itemPageUIs.item_craft_input import CraftInputUI
from GUI.itemPageUIs.item_craft_display import CraftDisplayUI


class CraftItemUI:
    def __init__(self, parent, frame):
        self.parent = parent
        self.frame = frame

        # Header Frame
        self.header_frame = ttk.Frame(self.frame)
        self.header_frame.pack(pady=(0, 10))

        ttk.Label(self.header_frame, text="Craft Item", style="tab_header.TLabel") \
            .grid(column=0, row=0)
        ttk.Label(
            self.header_frame,
            text="Convert old items into newer and stronger one!",
            style="tab_subtitle.TLabel"
        ) \
            .grid(column=1, row=0, sticky="s", padx=10, pady=5)

        # Content Frame
        self.content_frame = ttk.Frame(self.frame)
        self.content_frame.pack(expand=True, fill="both")

        # Input Section
        self.craft_input_frame = ttk.Frame(self.content_frame)
        self.craft_input_frame.grid(column=0, row=0)
        self.craft_input = CraftInputUI(self.content_frame, self.craft_input_frame)

        # Vertical Separator
        ttk.Separator(self.content_frame, orient="vertical").grid(column=1, row=0, sticky="ns", padx=25, pady=4)

        # Display Section
        self.craft_display_frame = ttk.Frame(self.content_frame)
        self.craft_display_frame.grid(column=2, row=0)
        self.craft_display = CraftDisplayUI(self.content_frame, self.craft_display_frame)
