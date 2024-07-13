import tkinter as tk

class Menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.add_button = tk.Button(
            self,
            bitmap="@data/icons/plus_24.xbm"
        )
        self.buttons.append(self.add_button)
        self.add_button.grid(row=0, column=0)

        self.time_button = tk.Button(
            self,
            bitmap="@data/icons/time_24.xbm"
        )
        self.buttons.append(self.time_button)
        self.time_button.grid(row=0, column=1)

        self.categories_button = tk.Button(
            self,
            bitmap="@data/icons/folder_24.xbm"
        )
        self.buttons.append(self.categories_button)
        self.categories_button.grid(row=0, column=2)

        self.colors_button = tk.Button(
            self,
            bitmap="@data/icons/palette_24.xbm"
        )
        self.buttons.append(self.colors_button)
        self.colors_button.grid(row=0, column=3)

        self.settings_button = tk.Button(
            self,
            bitmap="@data/icons/gears_24.xbm"
        )
        self.buttons.append(self.settings_button)
        self.settings_button.grid(row=0, column=4)

    def refresh_colors(self, colors):
        for button in self.buttons:
            button.configure(
                foreground=colors["HL2"],
                background=colors["BG2"]
            )

        self.master.configure(background=colors["BG2"])