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
from tkinter import ttk, messagebox

# External GUI file imports:
from playerPage import PlayerPage
from bossPage import BossPage
from styling import *


class MainUI:
    def __init__(self):
        # Main GUI Frame
        self.root = tk.Tk()
        self.root.title("Game Kradad - Gameplay Assisting Program")
        self.root.iconbitmap("../ico/gkne-mainap-ce-icon.ico")
        self.root.geometry("+200+30")

        # Styling
        self.styling = Styling(self.root)

        # Main Page Notebook
        self.main_book = ttk.Notebook(self.root)
        self.main_book.pack(fill="both", expand=True)

        # Main Page Category

        # Player TODO: Build player page with functionality similar to playerStat.py
        self.player_page_frame = ttk.Frame(self.main_book)
        self.player_page = PlayerPage(self.root, self.main_book, self.player_page_frame)
        self.player_page_frame.pack(fill="both", expand=True)
        # self.player_page_frame.grid()
        # self.player_page_frame.rowconfigure('all', weight=1)
        # self.player_page_frame.columnconfigure('all', weight=1)

        # Boss TODO: Build boss page with functionality similar to bossStat.py
        self.boss_page_frame = ttk.Frame(self.main_book)
        self.boss_page = BossPage(self.main_book, self.boss_page_frame)
        self.boss_page_frame.pack(fill="both", expand=True)
        # self.boss_page_frame.grid()
        # self.boss_page_frame.rowconfigure('all', weight=1)
        # self.boss_page_frame.columnconfigure('all', weight=1)

        # Item TODO: Build item page with functionality similar to itemStat.py

        # TODO: Add each frame in the Main Page Category section into the Notebook
        self.main_book.add(self.player_page_frame, text="Player")
        self.main_book.add(self.boss_page_frame, text="Boss")
        # main_book.add(item_page, text="Item")

    def run(self):
        self.root.mainloop()
