"""
***********************************************

Author: MontyGUI

Description:
This script extends itemPage.py and is a child section of item_dropped_item.py,
it includes the layout and functions of the interface
that displays the generated crafted item

***********************************************
"""

import tkinter as tk
from tkinter import ttk

ITEM_TYPE_MAPPING = {
    "wpn": "Weapon",
    "amr": "Armor",
    "acc": "Accessories"
}

ITEM_QUALITY_MAPPING = {
    -7: "Bad",
    0: "Normal",
    7: "Great"
}


class CraftDisplayUI:
    def __init__(self, parent, frame):
        self.parent = parent
        self.frame = frame

        # Display Label Frame
        self.lbf = ttk.LabelFrame(self.frame, text="Item")
        self.lbf.pack(expand=True, fill="both")

        # Placeholder Frame
        self.placeholder_frame = ttk.Frame(self.lbf)
        self.placeholder_frame.pack(expand=True, fill="both")
        ttk.Label(self.placeholder_frame, text="Crafted Item will be displayed here.") \
            .pack(expand=True, fill="both", padx=20, pady=80)

        # Content Frame
        self.content_frame = ttk.Frame(self.lbf)
        self.content_frame.pack(expand=True, fill="both", padx=60)

        # Type & Label Row
        self.qtl_box = ttk.Label(self.content_frame, text="[QUALITY] [TYPE] - LV [LV]", style="category_txt.TLabel")
        self.qtl_box.grid(column=0, row=0, columnspan=3)

        # HP Row
        ttk.Label(self.content_frame, text="HP: ", style="category_txt.TLabel") \
            .grid(column=0, row=1, padx=4, pady=5)
        self.hp_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.hp_box.grid(column=1, row=1, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=1, padx=4)

        # PATK Row
        ttk.Label(self.content_frame, text="P. ATK: ", style="category_txt.TLabel") \
            .grid(column=0, row=2, padx=4, pady=5)
        self.patk_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.patk_box.grid(column=1, row=2, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=2, padx=4)

        # MATK Row
        ttk.Label(self.content_frame, text="M. ATK: ", style="category_txt.TLabel") \
            .grid(column=0, row=3, padx=4, pady=5)
        self.matk_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.matk_box.grid(column=1, row=3, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=3, padx=4)

        # PDEF Row
        ttk.Label(self.content_frame, text="P. DEF: ", style="category_txt.TLabel") \
            .grid(column=0, row=4, padx=4, pady=5)
        self.pdef_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.pdef_box.grid(column=1, row=4, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=4, padx=4)

        # MDEF Row
        ttk.Label(self.content_frame, text="M. DEF: ", style="category_txt.TLabel") \
            .grid(column=0, row=5, padx=4, pady=5)
        self.mdef_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.mdef_box.grid(column=1, row=5, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=5, padx=4)

        self.show_placeholder()

    def show_placeholder(self):
        self.content_frame.pack_forget()
        self.placeholder_frame.pack(expand=True, fill="both")

    def show_content(self):
        self.content_frame.pack(expand=True, fill="both", padx=40)
        self.placeholder_frame.pack_forget()

    def display(self, item):
        quality_text = ITEM_QUALITY_MAPPING.get(item['QUALITY'])
        type_text = ITEM_TYPE_MAPPING.get(item['TYPE'])

        self.qtl_box['text'] = f"{quality_text} Quality {type_text} - LV {item['LV']}"
        self.hp_box['text'] = item['HP']
        self.patk_box['text'] = item['PATK']
        self.matk_box['text'] = item['MATK']
        self.pdef_box['text'] = item['PDEF']
        self.mdef_box['text'] = item['MDEF']
        self.show_content()
