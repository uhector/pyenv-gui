# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from .components.notebook import Notebook

class MainFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.notebook = Notebook(self)

        parent.title("Pyenv Manager")
        self.pack()
