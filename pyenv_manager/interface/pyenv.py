# -*- coding: utf-8 -*-

import subprocess
import os

from . import helpers

class PyenvInterface:

    def __init__(self):
        self.root_dir = self._get_root_dir()
        self.versions_dir = os.path.join(self.root_dir, 'versions')

    def __new__(cls):
        is_installed = subprocess.run('pyenv --version',
                                      capture_output=True,
                                      shell=True)

        if is_installed.returncode == 0:
            return object.__new__(cls)
        else:
            return None


    def get_installed_versions(self):
        ps = subprocess.Popen(['ls', '-l',
                              self.versions_dir],
                              stdout=subprocess.PIPE)

        output = subprocess.check_output(['grep', '^d'],
                                      stdin=ps.stdout,
                                      text=True)

        return ['system'] + helpers.parse_ls_output(output)

    def get_global_version(self):
        with open(f'{self.root_dir}/version', 'r') as file:
            lines = []
            for line in file:
                lines.append(line)

        if len(lines) != 0:
            return lines[0]
        else:
            return 'system'

    def set_global_version(self, version):
        with open(f'{self.root_dir}/version', 'w') as file:
            file.write(version)

    def _get_root_dir(self):
        root_dir = subprocess.run('pyenv root',
                                  capture_output=True,
                                  shell=True,
                                  text=True)

        return root_dir.stdout[:-1]
