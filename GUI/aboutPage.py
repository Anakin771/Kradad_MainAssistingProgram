"""
***********************************************

Author: MontyGUI

Description:
This script includes the GUI of the About Page,
it includes the generic information about the Graphical Edition App, such as version,
author, date released, and copyright

***********************************************
"""
import webbrowser
from tkinter import ttk


class AboutPage:
    def __init__(self, root, frame, version):
        self.root = root
        self.frame = frame
        self.VERSION = version

        self.container = ttk.Frame(self.frame, relief="groove", borderwidth=3)
        self.container.pack(ipadx=100, ipady=20, padx=10, pady=10)

        ttk.Label(self.container, text="Game Kradad", style="tab_header.TLabel").pack()
        ttk.Label(self.container, text="Main Assisting Program", style="sub_header.TLabel").pack()
        ttk.Label(self.container, text=f"Graphical Edition - v{self.VERSION}", style="med_header.TLabel").pack(pady=10)

        ttk.Label(
            self.container,
            text="This Program is used for generating new character stats,\n"
                 "calculate levels, generating fights and items,\nand also craft items for players "
                 "in Game Kradad - 2nd Revision",
            style="placeholder.TLabel"
        ).pack(pady=10)

        ttk.Label(
            self.container,
            text="For more information about the program,\n"
                 "please visit the code's repository at",
            style="placeholder.TLabel"
        ).pack(pady=(10, 5))

        self.github_link = ttk.Label(
            self.container,
            text="https://github.com/Anakin771/Kradad_MainAssistingProgram/",
            font=('Helvetica bold', 15),
            foreground="blue",
            cursor="hand2"
        )
        self.github_link.pack(pady=(5, 10))
        self.github_link.bind(
            "<Button-1>",
            lambda e: self.link("https://github.com/Anakin771/Kradad_MainAssistingProgram/")
        )

        ttk.Label(
            self.container,
            text="Author: MontyGUI (Yanakorn Chaeyprasert)",
            style="category_txt.TLabel"
        ).pack(pady=15)

        ttk.Label(
            self.container,
            text="Copyright 2021 - MontyGUI",
            style="category_txt.TLabel"
        ).pack(pady=15)

    @staticmethod
    def link(url):
        webbrowser.open_new_tab(url)
