# -*- coding: utf-8 -*-

from tkinter import ttk

from .. import pyenv_interface

class Treeview(ttk.Treeview):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.heading('#0', text='Installed versions')


    def update(self):
        children = self.get_children()
        if children:
            for child in children:
                self.delete(child)

        for version in pyenv_interface.installed_versions:
            if version == pyenv_interface.get_global_version():
                version += '*'
            self.insert('', 0, text=version)
