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

# Main GUI Frame
main_frame = tk.Tk()
main_frame.title("Game Kradad - Gameplay Assisting Program")

# Main Page Category
# Player TODO: Build player page with functionality similar to playerStat.py
# Boss TODO: Build boss page with functionality similar to bossStat.py
# Item TODO: Build item page with functionality similar to itemStat.py

# Main Page Notebook
main_book = ttk.Notebook(main_frame)
# TODO: Add each frame in the Main Page Category section into the Notebook
# main_book.add(player_page, text="Player")
# main_book.add(boss_page, text="Boss")
# main_book.add(item_page, text="Item")


def run_main():
    main_frame.mainloop()
