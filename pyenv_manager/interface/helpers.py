# -*- coding: utf-8 -*-

def parse_ls_output(output):
    directories = []
    strings = output.split('\n')
    for string in strings:
        directories.append(string.split(' ')[-1])
    return directories[:-1]
