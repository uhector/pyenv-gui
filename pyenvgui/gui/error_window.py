import os

import tkinter as tk
from tkinter import ttk

from .img import IMG_PATH


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Main window config
        self.title("Error")
        self.resizable(False, False)
        self.icon = tk.PhotoImage(file=os.path.join(IMG_PATH, 'icon.png'))
        self.call('wm', 'iconphoto', self._w, self.icon)

        # Widgets
        tk.Label(
            self, text='pyenv is not installed on your system.'
        ).grid(column=0, row=0, padx=10, pady=10)

        ttk.Button(
            self, text='Exit', command=self.destroy
        ).grid(column=0, row=1, padx=10, pady=10)
