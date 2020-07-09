from threading import Thread

import tkinter as tk
from tkinter import ttk, messagebox

from . import pyenv
from ._custom_widgets import Treeview


class VersionManagementFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Installed versions options
        self.installed_options = ttk.LabelFrame(
            self, text='Installed versions'
        )

        self.tree = Treeview(self.installed_options)
        self.tree.grid(column=0, row=0, columnspan=2)
        
        self.tree.insert_items(
           list(pyenv.installed) + ['system'],
           highlight=pyenv.global_version[0]
        )

        ttk.Button(
            self.installed_options,
            text='Set as global',
            command=lambda: self._set_as_global(
                                self.tree.selected_item
                            )
        ).grid(column=0, row=1, sticky="nsew")

        ttk.Button(
            self.installed_options, text='Uninstall',
            command=lambda: self._uninstall(
                                self.tree.selected_item
                            )
        ).grid(column=1, row=1, sticky="nsew")

        self.installed_options.grid(column=0, row=0)

        # Install a new version options
        self.install_options = ttk.LabelFrame(
            self, text='Install a new version'
        )
        self.versions_combo = ttk.Combobox(
            self.install_options, state="readonly"
        )
        self.versions_combo.set(' Select a version...')
        self.versions_combo['values'] = pyenv.available
        self.versions_combo.grid(column=0, row=1, sticky="nsew", padx=5)

        self.install_button = ttk.Button(
            self.install_options,
            text='Install',
            command=lambda: Thread(
                target=self._start_installation,
                args=(self.versions_combo.get(),)
            ).start()
        )
        self.install_button.grid(column=1, row=1, sticky="nsew", padx=5)

        tk.Label(
            self.install_options, text='Logs:'
        ).grid(column=0, row=2, pady=(5, 1))

        self.terminal_output = tk.Text(
            self.install_options,
            font=("Helvetica", 8),
            height=17,
            width=70
        )
        self.terminal_output.grid(column=0, row=3, columnspan=2)
        self.terminal_output.grid_propagate(False)
        
        self.install_options.grid(column=1, row=0, sticky='ns')

    def _set_as_global(self, version):
        version = version['text'][2:]

        if version and version != pyenv.global_version[0]:
            if pyenv.global_version[0] is not version:
                if version == 'system':
                    del pyenv.global_version
                else:
                    pyenv.global_version = [version]
        
            self.tree.clean()
            self.tree.insert_items(
                list(pyenv.installed) + ['system'],
                highlight=version
            )

    def _uninstall(self, version):
        version = version['text'][2:]

        if version:
            if version == 'system':
                messagebox.showerror(
                    title='Error',
                    message='You can not uninstall the system version from here.'
                )

            else:
                op = messagebox.askquestion(
                        title='Uninstall',
                        message=f'Are you sure you want to uninstall version {version}?'
                    )

                if op == 'yes':
                    pyenv.uninstall(version)
                    
                    if version == pyenv.global_version[0]:
                        del pyenv.global_version
                    
                    self.tree.clean()
                    self.tree.insert_items(
                        list(pyenv.installed) + ['system'],
                        highlight=pyenv.global_version[0]
                    )

                    messagebox.showinfo(
                        title='Uninstall',
                        message=f'{version} version has been uninstalled.'
                    )

    def _start_installation(self, version):
        if version and version != ' Select a version...':
            self.install_button.config(state='disable')

            ps = None

            if version in pyenv.installed:
                op = messagebox.askquestion(
                        title='Install',
                        message=f'Version {version} already exists.\nDo you want to continue?'
                    ) 

                if op == 'yes':
                    ps = pyenv.install(version, verbose=True, force=True)
            else:
                ps = pyenv.install(version, verbose=True)

            if ps:
                self.terminal_output.delete('1.0', tk.END)

                while ps.poll() == None:
                    output = ps.stdout.readline().decode()

                    if output:
                        self.terminal_output.insert(tk.END, output)
                        self.terminal_output.see(tk.END)

                if ps.returncode:
                    messagebox.showerror(
                        title='Install',
                        message='Something went wrong during the installation.'
                    )
                else:
                    messagebox.showinfo(
                        title='Install',
                        message=f'Python {version} was installed successfully.'
                    )

            self.tree.clean()
            self.tree.insert_items(
                list(pyenv.installed) + ['system'],
                highlight=pyenv.global_version[0]
            )
            self.install_button.config(state='normal')
