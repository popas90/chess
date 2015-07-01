from tkinter import *


class SquareView(Button):

    def __init__(self, master, name, **kwargs):
        Button.__init__(self, master, **kwargs)
        self.name = name