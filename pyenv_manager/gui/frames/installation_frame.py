# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from threading import Thread

from .. import pyenv_interface
from ..components.combobox import Combobox
from ..components.text import Text

class InstallationFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text='Select a version').pack()

        self.versions_combo = Combobox(self, state="readonly")

        self.install_button = ttk.Button(
            self,
            text='Install',
            command=lambda: Thread(
                target=self.start_installation
            ).start()
        )

        self.install_button.pack()

        self.terminal_output = tk.Text(self, height=10, width=50)
        self.terminal_output.pack()

        self.pack()


    def start_installation(self):
        selected_version = self.versions_combo.get()

        if selected_version:
            self.install_button.config(state='disable')

            ps = pyenv_interface.install(selected_version)

            while not ps.poll():
                output = ps.stdout.readline().decode()
                self.terminal_output.insert(tk.END, output)
                self.terminal_output.see(tk.END)

        self.install_button.config(state='normal')
