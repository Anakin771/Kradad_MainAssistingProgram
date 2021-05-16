"""
***********************************************

Author: MontyGUI

Description
This script includes the GUI Main Control Panel, it
combines all other GUI scripts found within GUI folder
and merge it into a single Desktop Application layout

***********************************************
"""
import tkinter as tk
from tkinter import ttk

# External GUI file imports:
from playerPage import PlayerPage
from bossPage import BossPage
from itemPage import ItemPage
from styling import Styling

VERSION = "1.0.0"


class MainUI:
    def __init__(self):
        # Main GUI Frame
        self.root = tk.Tk()
        self.root.title(f"Game Kradad - Main Assisting Program (v{VERSION})")
        self.root.iconbitmap("../ico/gkne-mainap-ce-icon.ico")
        self.root.geometry("+200+30")

        # Styling
        self.styling = Styling(self.root)

        # Main Page Notebook
        self.main_book = ttk.Notebook(self.root)
        self.main_book.pack(fill="both", expand=True)

        # Main Page Category

        # Player
        self.player_page_frame = ttk.Frame(self.main_book)
        self.player_page = PlayerPage(self.root, self.main_book, self.player_page_frame)
        self.player_page_frame.pack(fill="both", expand=True)

        # Boss
        self.boss_page_frame = ttk.Frame(self.main_book)
        self.boss_page = BossPage(self.root, self.boss_page_frame)
        self.boss_page_frame.pack(fill="both", expand=True)

        # Item TODO: Build item page with functionality similar to itemStat.py
        self.item_page_frame = ttk.Frame(self.main_book)
        self.item_page = ItemPage(self.root, self.item_page_frame)
        self.item_page_frame.pack(fill="both", expand=True)

        # Add each Frame into the Notebook Widget
        self.main_book.add(self.player_page_frame, text="Player")
        self.main_book.add(self.boss_page_frame, text="Boss")
        self.main_book.add(self.item_page_frame, text="Item")

    def run(self):
        self.root.mainloop()
