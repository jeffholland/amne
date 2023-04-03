import tkinter as tk

from colors import Colors
from fonts import Fonts

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        self.calculate_dims()
        self.get_colors()
        self.set_fonts()

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(
            self, 
            text="amne", 
            foreground=self.colors["HL2"],
            background=self.colors["BG2"],
            font=self.default_font
        )
        label.grid(
            row=0, 
            column=0,
            ipadx=10,
            ipady=10,
            sticky=tk.NSEW
        )
        self.columnconfigure(0, minsize=self.width)

        self.master.configure(background=self.colors["BG2"])

    def calculate_dims(self):
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        w_num_div = 6
        h_num_div = 6

        w_div = self.screen_width // w_num_div
        h_div = self.screen_height // h_num_div

        self.width = w_div
        self.height = h_div
        self.x_offset = w_div * (w_num_div - 1)

    def get_colors(self):
        self.colors_obj = Colors(self)
        self.colors = self.colors_obj.colors

    def set_fonts(self):
        self.fonts_obj = Fonts(self)
        self.default_font = self.fonts_obj.default_font


app = Application()
app.master.title("amne")
app.master.geometry(f"{app.width}x{app.height}+{app.x_offset}+0")
app.mainloop()