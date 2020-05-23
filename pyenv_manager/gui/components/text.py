# -*- coding: utf-8 -*-

import tkinter as tk

class Text(tk.Text):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
