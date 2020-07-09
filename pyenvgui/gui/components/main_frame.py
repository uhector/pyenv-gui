from tkinter import ttk

from ._about import AboutFrame
from ._version_management import VersionManagementFrame


class MainFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.notebook = ttk.Notebook(self)

        # Notebook tabs
        self.notebook.add(
            VersionManagementFrame(self),
            text='Version Management'
        )

        self.notebook.add(
            AboutFrame(self),
            text='About'
        )

        self.notebook.pack()
