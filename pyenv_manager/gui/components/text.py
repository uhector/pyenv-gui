# -*- coding: utf-8 -*-

import tkinter as tk
import time

class Text(tk.Text):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def insert_text(self, text):
        self.insert(tk.END, text)

    def insert_from_file(self, interface):
        while interface.installing_version:
            with open('logs.txt', 'r') as file:
                self.config(state='normal')
                self.clean()
                self.insert_text(file.read())
                self.scroll_down()
                self.config(state='disable')
            time.sleep(1)

    def clean(self):
        self.delete(1.0, tk.END)

    def scroll_down(self):
        self.see(tk.END)