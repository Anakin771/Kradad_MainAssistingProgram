"""
***********************************************

Author: MontyGUI

Description
This script extends itemPage.py,
it includes the layout and functions of the interface
that generates a dropped item from a boss.

***********************************************
"""

from tkinter import ttk

from GUI.itemPageUIs.item_dropped_input import DroppedInputUI
from GUI.itemPageUIs.item_dropped_display import DroppedDisplayUI


class DroppedItemUI:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Heading
        # Head Layer
        self.header_frame = ttk.Frame(self.frame)
        self.header_frame.pack(pady=(0, 10))

        ttk.Label(self.header_frame, text="Generate Dropped Item", style="tab_header.TLabel")\
            .grid(column=0, row=0)
        ttk.Label(self.header_frame, text="Get your loot!", style="tab_subtitle.TLabel")\
            .grid(column=1, row=0, sticky="s", padx=10, pady=5)

        # Content Section
        self.content_frame = ttk.Frame(self.frame)
        self.content_frame.pack(expand=True, fill="both")

        # Input Section
        self.input_frame = ttk.Frame(self.content_frame)
        self.input_frame.grid(column=0, row=0, padx=15, pady=5)
        self.input = DroppedInputUI(self.root, self.input_frame, None)

        # Vertical Separator
        ttk.Separator(self.content_frame, orient="vertical").grid(column=1, row=0, sticky="ns", padx=25, pady=4)

        # Item Display Section
        self.display_frame = ttk.Frame(self.content_frame)
        self.display_frame.grid(column=2, row=0, padx=15, pady=5)
        self.display = DroppedDisplayUI(self.root, self.display_frame)

        # Linking
        self.input.display_ui = self.display
