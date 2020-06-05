# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

import threading

from .. import pyenv_interface
from ..components.combobox import Combobox
from ..components.text import Text

class InstallationFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text='Select a version').pack()

        self.versions_combo = Combobox(self, state="readonly")

        ttk.Button(
            self,
            text='Install',
            command=self.start_installation
        ).pack()

        self.terminal_output = tk.Text(self, height=10, width=50)
        
        self.terminal_output.pack()

        self.pack()


    def start_installation(self):
        selected_version = self.versions_combo.get()
        
        installation = threading.Thread(
            target=pyenv_interface.install,
            args=(selected_version,)
        )

        update_text_widget = threading.Thread(
            target=self.terminal_output.insert_from_file,
            args=('logs.txt', pyenv_interface)
        )

        installation.start()
        update_text_widget.start()
