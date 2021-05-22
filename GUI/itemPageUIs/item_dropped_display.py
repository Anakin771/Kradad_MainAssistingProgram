"""
***********************************************

Author: MontyGUI

Description:
This script extends itemPage.py and is a child section of item_dropped_item.py,
it includes the layout and functions of the interface
that displays the generated dropped item

***********************************************
"""
import random
from tkinter import ttk

ITEM_TYPE_MAPPING = {
    "wpn": "Weapon",
    "amr": "Armor",
    "acc": "Accessories"
}

JIGGLE_LIMIT = 25


class DroppedDisplayUI:
    def __init__(self, root, frame, version, input_ui=None):
        self.root = root
        self.frame = frame
        self.input_ui = input_ui
        self.VERSION = version

        self.jiggle = 0
        self.animation = None

        # Display Label Frame
        self.lbf = ttk.LabelFrame(self.frame, text="Item")
        self.lbf.pack(expand=True, fill="both")

        # Placeholder Frame
        self.placeholder_frame = ttk.Frame(self.lbf)
        self.placeholder_frame.pack(expand=True, fill="both")
        ttk.Label(self.placeholder_frame, text="Generated Item will be displayed here.")\
            .pack(expand=True, fill="both", padx=20, pady=80)

        # Content Frame
        self.content_frame = ttk.Frame(self.lbf)
        self.content_frame.pack(expand=True, fill="both", padx=100, ipadx=100)

        # Type & Level Row
        self.type_lv_box = ttk.Label(self.content_frame, text="[TYPE] - LV [LV]", style="category_txt.TLabel")
        self.type_lv_box.grid(column=0, row=0, columnspan=3)

        # HP Row
        ttk.Label(self.content_frame, text="HP: ", style="category_txt.TLabel")\
            .grid(column=0, row=1, padx=4, pady=5)
        self.hp_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.hp_box.grid(column=1, row=1, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=1, padx=4)

        # PATK Row
        ttk.Label(self.content_frame, text="P. ATK: ", style="category_txt.TLabel")\
            .grid(column=0, row=2, padx=4, pady=5)
        self.patk_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.patk_box.grid(column=1, row=2, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=2, padx=4)

        # MATK Row
        ttk.Label(self.content_frame, text="M. ATK: ", style="category_txt.TLabel")\
            .grid(column=0, row=3, padx=4, pady=5)
        self.matk_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.matk_box.grid(column=1, row=3, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=3, padx=4)

        # PDEF Row
        ttk.Label(self.content_frame, text="P. DEF: ", style="category_txt.TLabel")\
            .grid(column=0, row=4, padx=4, pady=5)
        self.pdef_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.pdef_box.grid(column=1, row=4, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=4, padx=4)

        # MDEF Row
        ttk.Label(self.content_frame, text="M. DEF: ", style="category_txt.TLabel")\
            .grid(column=0, row=5, padx=4, pady=5)
        self.mdef_box = ttk.Label(self.content_frame, text="+??", style="category_txt.TLabel")
        self.mdef_box.grid(column=1, row=5, padx=4)
        ttk.Label(self.content_frame, text="pts.", style="category_txt.TLabel").grid(column=2, row=5, padx=4)

        self.show_placeholder()

    def show_placeholder(self):
        self.content_frame.pack_forget()
        self.placeholder_frame.pack(expand=True, fill="both")

    def show_content(self):
        self.content_frame.pack(expand=True, fill="both", padx=50)
        self.placeholder_frame.pack_forget()

    def display(self, item):
        type_text = ITEM_TYPE_MAPPING.get(item['TYPE'], "????")
        self.type_lv_box['text'] = f"{type_text} - LV {item['LV']}"
        self.hp_box['text'] = f"{item['HP']}"
        self.patk_box['text'] = f"{item['PATK']}"
        self.matk_box['text'] = f"{item['MATK']}"
        self.pdef_box['text'] = f"{item['PDEF']}"
        self.mdef_box['text'] = f"{item['MDEF']}"
        self.show_content()

    def animate(self, callback):
        if self.jiggle == 0:
            self.input_ui.generate_btn.configure(state="disabled")
            callback()

        if self.jiggle >= JIGGLE_LIMIT:
            self.content_frame.after_cancel(self.animation)
            self.animation = None
            self.jiggle = 0
            self.input_ui.generate_btn.configure(state="enabled")
            callback()
        else:
            num1, num2, num3, num4, num5 = random.sample(range(1, 1000), 5)
            self.hp_box['text'] = str(num1)
            self.patk_box['text'] = str(num2)
            self.matk_box['text'] = str(num3)
            self.pdef_box['text'] = str(num4)
            self.mdef_box['text'] = str(num5)
            self.jiggle += 1
            self.input_ui.generate_btn.configure(state="disabled")
            self.animation = self.content_frame.after(50, lambda: self.animate(callback))
