# -*- coding: utf-8 -*-

from tkinter import ttk

from ..components.treeview import Treeview

from .. import pyenv_interface

class VersionManagementFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.treeview = Treeview(self)
        self.treeview.grid(column=0, row=0, columnspan=2)
        self.treeview.update()

        ttk.Button(self, text='Set as global',
                   command=self._set_as_global).grid(column=0, row=1)

        ttk.Button(self, text='Install version').grid(column=1, row=1)

        self.pack()


    def _set_as_global(self):
        tree = self.treeview
        selected_version = tree.item(tree.selection())['text']
        if pyenv_interface.get_global_version() == selected_version[:-1]:
            pass
        else:
            if selected_version == 'system':
                pyenv_interface.set_global_version('')
            else:
                pyenv_interface.set_global_version(selected_version)
        tree.update()
