# -*- coding: utf-8 -*-

import tkinter as tk

from .frames.main_frame import MainFrame

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pyenv Manager")
        self.frame = MainFrame(self)
