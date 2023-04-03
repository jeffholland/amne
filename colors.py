import json

from constants import COLORS_PATH

class Colors:
    def __init__(self, master):
        self.master = master

        self.load_colors("default.json")

    def load_colors(self, filename):
        with open(COLORS_PATH + filename) as file:
            data = json.load(file)
            self.colors = data