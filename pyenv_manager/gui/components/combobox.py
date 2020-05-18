# -*- coding: utf-8 -*-

from tkinter import ttk

from .. import pyenv_interface

class Combobox(ttk.Combobox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pack()
