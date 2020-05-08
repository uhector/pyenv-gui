# -*- coding: utf-8 -*-

import subprocess
import os

from . import helpers

class PyenvInterface:

    def __init__(self):
        self.root_dir = self._get_root_dir()
        self.versions_dir = os.path.join(self.root_dir, 'versions')
        self.installed_versions = self._get_installed_versions()

    def __new__(cls):
        is_installed = subprocess.run('pyenv',
                                      capture_output=True,
                                      shell=True)

        if is_installed.returncode > 1:
            return None
        else:
            return object.__new__(cls)


    def _get_installed_versions(self):
        ps = subprocess.Popen(['ls', '-l',
                              self.versions_dir],
                              stdout=subprocess.PIPE)

        output = subprocess.check_output(['grep', '^d'],
                                      stdin=ps.stdout,
                                      text=True)

        return ['system'] + helpers.parse_ls_output(output)

    def _get_root_dir(self):
        root_dir = subprocess.run('pyenv root',
                                  capture_output=True,
                                  shell=True,
                                  text=True)

        return root_dir.stdout[:-1]
