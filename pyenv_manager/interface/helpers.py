# -*- coding: utf-8 -*-

def parse_ls_output(output):
    directories = []
    strings = output.split('\n')
    for string in strings:
        directories.append(string.split(' ')[-1])
    return directories[:-1]

def parse_output(output):
    result = []
    strings = output.split('\n')
    del strings[0]
    del strings[-1]
    for string in strings:
        if string[2].isnumeric():
            result.append(string.strip())
    return result
