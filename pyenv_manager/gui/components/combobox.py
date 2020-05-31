# -*- coding: utf-8 -*-

from tkinter import ttk

from .. import pyenv_interface

class Combobox(ttk.Combobox):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_values()
        self.pack()


    def add_values(self):
        self['values'] = pyenv_interface.avalible_versions
