"""
***********************************************

Author: MontyGUI

Description
This script includes the styling of the GUI of ALL Pages.
This file is included into the master page (mainFrame.py).
***********************************************
"""

import tkinter as tk
from tkinter import ttk, messagebox, font


class Styling:
    def __init__(self, root):
        self.root = root

        # Generic
        ttk.Style().configure("tab_header.TLabel", font=("Lucida Bright", 28, "bold"))
        ttk.Style().configure("tab_subtitle.TLabel", font=("Lucida Bright", 12, "italic"))
        ttk.Style().configure("TNotebook.Tab", font=("Helvetica", 12), width=10, anchor="center")

        # Player: Starting Stats
        ttk.Style().configure("strts_stat.TLabel", font=("Helvetica", 12, "bold"))
        ttk.Style().configure("strts_text.TLabel", font=("Lucida Bright", 10, "bold"))

        # Player: Bonus Rate
        ttk.Style().configure("bnrp_stat.TLabel", font=("Helvetica", 12, "bold"))
        ttk.Style().configure("bnrp_text.TLabel", font=("Lucida Bright", 10, "bold"))

        # Player: Level Up
        ttk.Style().configure("lu_category.TLabel", font=("Helvetica", 12, "bold"))
        ttk.Style().configure("lu_lv_up_msg.TLabel", font=("Helvetica", 12))
        ttk.Style().configure("lu_footnote.TLabel", font=("Helvetica", 10))
