# -*- coding: utf-8 -*-

from tkinter import ttk

from ..components.notebook import Notebook

class MainFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.notebook = Notebook(self)
        self.pack()
