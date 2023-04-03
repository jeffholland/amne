import tkinter.font as tkFont

class Fonts:
    def __init__(self, master):
        self.master = master
        self.default_font = tkFont.Font(
            self.master,
            font=("Helvetica", 24)
        )