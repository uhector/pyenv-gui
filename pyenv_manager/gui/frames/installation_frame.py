# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

class InstallationFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text='Select a version').pack()

        self.versions_combo = ttk.Combobox(self, state="readonly")
        self.versions_combo.pack()

        ttk.Button(self, text='Install').pack()

        self.terminal_output = tk.Text(self, height=10, width=50,
                                       state='disable')
        self.terminal_output.pack()

        self.pack()
