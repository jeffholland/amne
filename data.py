import json
from constants import NOTES_PATH

class Data:
    def __init__(self, master):
        self.master = master

    def get_notes_data(self, filename):
        with open(NOTES_PATH + filename) as file:
            data = json.load(file)
            return data