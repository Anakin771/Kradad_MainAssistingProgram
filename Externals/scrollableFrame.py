"""
********************************

Tkinter Scrollable Frame Kit
(Some extension were made by the author, please check Source for original)

Source: https://blog.teclado.com/tkinter-scrollable-frames/

********************************
"""
import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        x_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = ttk.Frame(self.canvas, relief="groove")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.recalibrate()
        )

        self.mid_x = self.canvas.winfo_screenwidth() / 2
        self.mid_y = self.canvas.winfo_screenheight() / 2

        self.scrollable_frame.pack(expand=True, fill="both")
        self.canvas.create_window((self.mid_x, self.mid_y), window=self.scrollable_frame, anchor="center")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.configure(xscrollcommand=x_scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        x_scrollbar.pack(side="bottom", fill="x")
        scrollbar.pack(side="right", fill="y")

    def recalibrate(self, **kwargs):
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

