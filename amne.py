import tkinter as tk

from constants import PADDING, W_NUM_DIV, H_NUM_DIV
from colors import Colors
from data import Data
from fonts import Fonts
from menu import Menu

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        self.calculate_dims()
        self.get_colors()
        self.set_fonts()
        self.get_data()

        self.create_widgets()
        self.refresh_colors(self.colors)


    def create_widgets(self):
        self.menu = Menu(self)
        self.menu.grid(row=0, column=0)

        self.label = tk.Label(
            self, 
            text=self.default_data[1], 
            wraplength=self.width - (PADDING * 2),
            font=self.default_font
        )
        self.label.grid(
            row=1, 
            column=0,
            ipadx=PADDING,
            ipady=PADDING,
            sticky=tk.NSEW
        )
        self.columnconfigure(0, minsize=self.width)


    def refresh_colors(self, colors):
        self.menu.refresh_colors(colors)

        self.label.configure(
            foreground=self.colors["HL2"],
            background=self.colors["BG2"]
        )

        self.master.configure(background=self.colors["BG2"])


    def calculate_dims(self):
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        w_div = self.screen_width // W_NUM_DIV
        h_div = self.screen_height // H_NUM_DIV

        self.width = w_div
        self.height = h_div
        self.x_offset = w_div * (W_NUM_DIV - 1)

    def get_colors(self):
        self.colors_obj = Colors(self)
        self.colors = self.colors_obj.colors

    def set_fonts(self):
        self.fonts_obj = Fonts(self)
        self.default_font = self.fonts_obj.default_font

    def get_data(self):
        self.data_obj = Data(self)
        self.default_data = self.data_obj.get_notes_data("computers.json")


app = Application()
app.master.title("amne")
app.master.geometry(f"{app.width}x{app.height}+{app.x_offset}+0")
app.mainloop()