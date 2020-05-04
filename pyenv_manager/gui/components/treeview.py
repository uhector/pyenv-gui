# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

class Treeview(ttk.Treeview):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.heading('#0', text='Installed versions')
