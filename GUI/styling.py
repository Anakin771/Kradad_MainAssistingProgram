"""
***********************************************

Author: MontyGUI

Description
This script includes the styling of the GUI of ALL Pages.
This file is included into the master page (mainFrame.py).

***********************************************
"""

from tkinter import ttk


class Styling:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style(self.root)

        # Generic
        self.style.configure("tab_header.TLabel", font=("Lucida Bright", 28, "bold"))
        self.style.configure("tab_subtitle.TLabel", font=("Lucida Bright", 12, "italic"))
        self.style.configure("TNotebook.Tab", font=("Helvetica", 12), width=10, anchor="center")
        self.style.configure("med_header.TLabel", font=("Lucida Bright", 10, "bold"))
        self.style.configure("category_txt.TLabel", font=("Helvetica", 12, "bold"))
        self.style.configure("placeholder.TLabel", font=("Helvetica", 14))

        # Player: Starting Stats
        self.style.configure("strts_stat.TLabel", font=("Helvetica", 12, "bold"))
        self.style.configure("strts_text.TLabel", font=("Lucida Bright", 10, "bold"))

        # Player: Bonus Rate
        self.style.configure("bnrp_stat.TLabel", font=("Helvetica", 12, "bold"))
        self.style.configure("bnrp_text.TLabel", font=("Lucida Bright", 10, "bold"))

        # Player: Level Up
        self.style.configure("lu_category.TLabel", font=("Helvetica", 12, "bold"))
        self.style.configure("lu_lv_up_msg.TLabel", font=("Helvetica", 12))
        self.style.configure("lu_footnote.TLabel", font=("Helvetica", 10))

        # Boss Display
        self.style.configure("single_boss_header.TLabel", font=("Lucida Bright", 20, "bold"))
        self.style.configure("single_boss_subheader.TLabel", font=("Helvetica", 18, "bold"))
        self.style.configure("single_boss_stat.TLabel", font=("Helvetica", 16, "bold"))
        self.style.configure("multi_display.Treeview.Heading", font=("Lucida Bright", 14, "bold"))
        self.style.configure("multi_display.Treeview", font=("Helvetica", 16, "bold"), rowheight=50)
        self.style.configure("multi_header.TLabel", font=("Lucida Bright", 20, "bold"))
