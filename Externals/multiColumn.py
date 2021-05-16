"""
Here the TreeView widget is configured as a multi-column listbox
with adjustable column width and column-header-click sorting.
"""
try:
    import Tkinter as tk
    import tkfont
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkfont
    import tkinter.ttk as ttk


class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(
            self,
            parent,
            frame,
            header,
            data_types,
            content,
            heading_txt=None,
            table_style="testStyle"
    ):
        self.parent = parent
        self.frame = frame
        self.header = header
        self.data_types = data_types
        self.content = content
        self.table_style = f"{table_style}.Treeview"
        if heading_txt is None:
            self.heading_txt = """Click on header to sort by that column
to change width of column drag boundary
        """
        else:
            self.heading_txt = heading_txt

        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(
            self.frame,
            columns=self.header,
            show="headings",
            style=self.table_style
        )
        vsb = ttk.Scrollbar(self.frame, orient="vertical",
                            command=self.tree.yview)
        hsb = ttk.Scrollbar(self.frame, orient="horizontal",
                            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
                            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        idx = 0

        for col in self.header:
            if self.data_types[idx]:
                self.tree.heading(col, text=col.upper(), command=lambda c=col: sortby_num(self.tree, c, 0))
            else:
                self.tree.heading(col, text=col.upper(), command=lambda c=col: sortby_str(self.tree, c, 0))
            self.tree.column(col, width=tkfont.Font().measure(col.title()), anchor="center")
            idx += 1

        for item in self.content:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkfont.Font().measure(val)
                if self.tree.column(self.header[ix], width=None) < col_w:
                    self.tree.column(self.header[ix], width=col_w)

    def update_list(self, new_list):
        self.content = new_list
        self.tree.delete(*self.tree.get_children())  # Clear all entries
        for item in self.content:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkfont.Font().measure(val)
                if self.tree.column(self.header[ix], width=None) < col_w:
                    self.tree.column(self.header[ix], width=col_w)


def sortby_str(tree, column, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, column), child) for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    # data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(column, command=lambda col=column: sortby_str(tree, col, int(not descending)))


def sortby_num(tree, column, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(float(tree.set(child, column)), child) for child in tree.get_children('')]
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(column, command=lambda col=column: sortby_num(tree, col, int(not descending)))


# if __name__ == '__main__':
#
#     car_header = ['car', 'repair', 'date']
#     car_list = [
#         ('Hyundai', 'brakes', '01/02/2013'),
#         ('Honda', 'light', '01/02/2013'),
#         ('Lexus', 'battery', '01/02/2013'),
#         ('Benz', 'wiper', '01/02/2013'),
#         ('Ford', 'tire', '01/02/2013'),
#         ('Chevy', 'air', '01/02/2013'),
#         ('Chrysler', 'piston', '01/02/2013'),
#         ('Toyota', 'brake pedal', '01/02/2013'),
#         ('BMW', 'seat', '01/02/2013'),
#         ('Chrysler', 'piston', '01/02/2013'),
#         ('Toyota', 'brake pedal', '01/02/2013')
#     ]
#
#     boss_header = ["boss", "HP", "P. ATK", "M. ATK", "P. DEF", "M. DEF"]
#     boss_hdr_dt_types = [0, 1, 1, 1, 1, 1]
#     boss_list = [
#         ("Boss #1", 25600, 200, 200, 200, 200),
#         ("Boss #2", 25600, 200, 200, 200, 200),
#         ("Boss #3", 25600, 200, 200, 200, 200),
#         ("Boss #4", 25600, 200, 200, 200, 200),
#         ("Boss #5", 25600, 200, 200, 200, 200),
#         ("Boss #6", 25600, 200, 200, 200, 200),
#         ("Boss #7", 25600, 200, 200, 200, 200),
#         ("Boss #8", 25600, 200, 200, 200, 200),
#         ("Boss #9", 25600, 200, 200, 200, 200),
#         ("Boss #10", 25600, 200, 200, 200, 200),
#         ("Boss #11", 25600, 200, 200, 200, 200)
#     ]
#     new_boss_list = [
#         ("Boss #1", 31500, 200, 200, 200, 200),
#         ("Boss #2", 45600, 200, 200, 200, 200),
#         ("Boss #3", 28600, 200, 200, 200, 200),
#         ("Boss #4", 25800, 200, 200, 200, 200),
#         ("Boss #5", 290000, 200, 200, 200, 200),
#         ("Boss #6", 256460, 200, 200, 200, 200),
#         ("Boss #7", 2565660, 200, 200, 200, 200),
#         ("Boss #8", 256600, 200, 200, 200, 200),
#         ("Boss #9", 2560000, 200, 200, 200, 200),
#         ("Boss #10", 2569500, 200, 200, 200, 200),
#         ("Boss #11", 2568700, 200, 200, 200, 200)
#     ]
#
#     root = tk.Tk()
#     root.title("Multicolumn Treeview/Listbox")
#
#     ttk.Style().configure("testStyle.Treeview.Heading", font=("Lucida Bright", 14, "bold"))
#     ttk.Style().configure("testStyle.Treeview", font=("Helvetica", 16, "bold"), rowheight=100)
#
#     # car_list_frame = ttk.Frame(root)
#     # car_listbox = MultiColumnListbox(root, car_list_frame, car_header, car_list, heading_txt="Car Repair List")
#     # car_list_frame.pack(expand=True, fill="both", padx=50)
#
#     boss_list_frame = ttk.Frame(root)
#     boss_listbox = MultiColumnListbox(
#         root,
#         boss_list_frame,
#         boss_header,
#         boss_hdr_dt_types,
#         boss_list,
#         heading_txt="Boss List"
#     )
#     boss_list_frame.pack(expand=True, fill="both", padx=80)
#     boss_listbox.update_list(new_boss_list)
#     root.mainloop()
