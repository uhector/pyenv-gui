# -*- coding: utf-8 -*-

import os
import subprocess

from . import helpers

class PyenvInterface:

    state = False

    def __init__(self):
        self.root_dir = self._get_root_dir()
        self.versions_dir = os.path.join(self.root_dir, 'versions')

    def __new__(cls):
        '''Check if pyenv is installed
        
        If it's installed, return a PyenvInterface object,
        if it's not installed, return None.
        '''

        check_pyenv = subprocess.run(['pyenv', '--version'],
                                     capture_output=True)

        if check_pyenv.returncode == 0:
            return object.__new__(cls)
        else:
            return None

    @property
    def installed_versions(self):
        ps = subprocess.Popen(['ls', '-l',
                              self.versions_dir],
                              stdout=subprocess.PIPE)

        output = subprocess.check_output(['grep', '^d'],
                                         stdin=ps.stdout,
                                         text=True)

        return ['system'] + helpers.parse_ls_output(output)

    @property
    def available_versions(self):
        ps = subprocess.run('pyenv install --list',
                            capture_output=True, shell=True)

        output = ps.stdout.decode()

        return helpers.parse_output(output)

    @property
    def global_version(self):
        with open(f'{self.root_dir}/version', 'r') as file:
            lines = []
            for line in file:
                lines.append(line)

        if len(lines) != 0:
            return lines[0]
        else:
            return 'system'

    @global_version.setter
    def global_version(self, version):
        with open(f'{self.root_dir}/version', 'w') as file:
            file.write(version)

    @classmethod
    def switch_state(cls):
        if cls.state:
            cls.state = False
        else:
            cls.state = True

    def install_version(self, version):
        '''This method only should be called in a different thread'''
        with open('logs.txt', 'w') as file:
            subprocess.run(['pyenv', 'install', version, '--verbose'],
                            stdout=file, text=True)

    def _get_root_dir(self):
        root_dir = subprocess.run('pyenv root',
                                  capture_output=True,
                                  shell=True,
                                  text=True)

        return root_dir.stdout[:-1]
