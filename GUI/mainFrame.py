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
import sys

# External GUI file imports:
from GUI.playerPage import PlayerPage
from GUI.bossPage import BossPage
from GUI.itemPage import ItemPage
from GUI.styling import Styling
from GUI.aboutPage import AboutPage


class MainUI:
    def __init__(self):

        self.VERSION = "1.0.0"

        # Main GUI Frame
        self.root = tk.Tk()
        self.root.title(f"Game Kradad - Main Assisting Program (v{self.VERSION})")

        # Check the directory of the interpreter path,
        # as the interpreter for venv and master python runs on a different directory
        # which is undetectable to __file__ or inspect stack
        interpreter_dir = str(sys.executable)
        if "venv" in interpreter_dir:
            # PyCharm Test Dir
            self.root.iconbitmap("../ico/gkne-mainap-ce-icon.ico")
        elif "venv" not in interpreter_dir:
            # App Dir
            self.root.iconbitmap("ico/gkne-mainap-ce-icon.ico")

        self.root.geometry("+200+30")

        # Styling
        self.styling = Styling(self.root)

        # Main Page Notebook
        self.main_book = ttk.Notebook(self.root)
        self.main_book.pack(fill="both", expand=True)

        # Main Page Category

        # Player
        self.player_page_frame = ttk.Frame(self.main_book)
        self.player_page = PlayerPage(self.root, self.player_page_frame, self.VERSION)
        self.player_page_frame.pack(fill="both", expand=True)

        # Boss
        self.boss_page_frame = ttk.Frame(self.main_book)
        self.boss_page = BossPage(self.root, self.boss_page_frame, self.VERSION)
        self.boss_page_frame.pack(fill="both", expand=True)

        # Item
        self.item_page_frame = ttk.Frame(self.main_book)
        self.item_page = ItemPage(self.root, self.item_page_frame, self.VERSION)
        self.item_page_frame.pack(fill="both", expand=True)

        # About
        self.about_page_frame = ttk.Frame(self.main_book)
        self.about_page = AboutPage(self.root, self.about_page_frame, self.VERSION)
        self.about_page_frame.pack(fill="both", expand=True)

        # Add each Frame into the Notebook Widget
        self.main_book.add(self.player_page_frame, text="Player")
        self.main_book.add(self.boss_page_frame, text="Boss")
        self.main_book.add(self.item_page_frame, text="Item")
        self.main_book.add(self.about_page_frame, text="About")

    def run(self):
        self.root.mainloop()
