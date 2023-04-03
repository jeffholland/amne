import tkinter.font as tkFont

from constants import DEFAULT_FONT_SIZE

class Fonts:
    def __init__(self, master):
        self.master = master
        self.default_font = tkFont.Font(
            self.master,
            font=("Helvetica", DEFAULT_FONT_SIZE)
        )