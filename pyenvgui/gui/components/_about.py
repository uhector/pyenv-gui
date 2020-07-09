import os

import tkinter as tk
from tkinter import ttk

from webbrowser import open_new

from ._version_management import VersionManagementFrame
from ..img import IMG_PATH
from ... import __version__

content = """
BSD 3-Clause License

Copyright (c) 2020, Ángel Llinas, Hector Ulacio
All rights reserved.
"""

class AboutFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.container = ttk.LabelFrame(self, text=f'pyenvGUI v{__version__}')

        self.canvas = tk.Canvas(self.container, width=64, height=64)
        self.image = tk.PhotoImage(file=os.path.join(IMG_PATH, 'icon.png'))
        self.canvas.create_image(33, 33, image=self.image) 
        self.canvas.pack()

        tk.Label(
            self.container,
            text=content,
            justify='center'
        ).pack()

        # GitHub link
        self.link = tk.Label(
            self.container,
            text="GitHub",
            fg="blue",
            cursor="hand2"
        )
        self.link.bind(
            "<Button-1>",
            lambda e: open_new("https://github.com/ulacioh/pyenv-gui")
        )
        self.link.pack()

        # Icon credits
        self.link2 = tk.Label(
            self.container,
            text="Icon made by Freepik from www.flaticon.com",
            fg="blue",
            cursor="hand2"
        )
        self.link2.bind(
            "<Button-1>",
            lambda e: open_new("https://www.flaticon.com/authors/freepik")
        )
        self.link2.pack()

        self.container.pack()
