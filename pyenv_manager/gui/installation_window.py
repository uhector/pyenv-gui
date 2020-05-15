# -*- coding: utf-8 -*-

import tkinter as tk

from .frames.installation_frame import InstallationFrame

class InstallationWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()

        self.title('Install version')
        self.frame = InstallationFrame(self)
