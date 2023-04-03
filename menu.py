import tkinter as tk

class Menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.time_button = tk.Button(
            self,
            bitmap="@data/time_24.xbm"
        )
        self.time_button.grid(row=0, column=0)

    def refresh_colors(self, colors):
        self.time_button.configure(
            foreground=colors["HL2"],
            background=colors["BG2"]
        )

        self.master.configure(background=colors["BG2"])