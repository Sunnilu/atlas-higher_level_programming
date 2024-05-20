#!/usr/bin/python3
'''Module to append a string.'''


def append_write(filename="", text=""):
    '''appends a string end of a text file (UTF8)returns number of characters added.'''
    with open(filename, mode='a', encoding= 'utf-8') as file:
        return file.write(text)
