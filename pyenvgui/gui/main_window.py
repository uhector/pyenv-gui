import os

import tkinter as tk

from .components import MainFrame
from .img import IMG_PATH


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Main window config
        self.title("pyenvGUI")
        self.resizable(False, False)
        self.icon = tk.PhotoImage(file=os.path.join(IMG_PATH, 'icon.png'))
        self.call('wm', 'iconphoto', self._w, self.icon)

        # Widgets
        self.frame = MainFrame(self)
        self.frame.pack()
