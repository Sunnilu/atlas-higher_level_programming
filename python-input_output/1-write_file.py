#!/usr/bin/python3
'''Reads a text file.'''


def write_file(filename="", text=""):
    '''Writes a string to a text file (UTF8) return number of characters.'''
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
