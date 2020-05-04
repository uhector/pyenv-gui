# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from .components.treeview import Treeview

class VersionManagementFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.treeview = Treeview(self)
        self.treeview.grid(column=0, row=0, columnspan=2)

        ttk.Button(self, text='Set as global').grid(column=0, row=1)
        ttk.Button(self, text='Install version').grid(column=1, row=1)

        self.pack()
