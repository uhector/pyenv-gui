# -*- coding: utf-8 -*-

from tkinter import ttk

from .. import pyenv_interface

class Treeview(ttk.Treeview):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.heading('#0', text='Installed versions')

    def clean(self):
        children = self.get_children()

        if children:
            for child in children:
                self.delete(child)

    def update(self):
        self.clean()

        for version in pyenv_interface.installed_versions:
            if version == pyenv_interface.global_version:
                version += '*'
            self.insert('', 0, text=version)
