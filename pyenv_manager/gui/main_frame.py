# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

class MainFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        parent.title("Pyenv Manager")
        self.pack()
