# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from .notebook_frames import VersionManagementFrame

class Notebook(ttk.Notebook):

    def __init__(self, parent):
        super().__init__(parent)

        # Version Management tab
        self.add(VersionManagementFrame(self),
                 text='Version Management',
                 padding=5
        )

        self.pack()
