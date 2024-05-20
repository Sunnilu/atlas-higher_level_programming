#!usr/bin/python3
'''Reads a text file.'''


def read_file(filename=""):
    '''Reads a text file using the (UTF8), and prints it to stdout.'''
    with open(filename, encoding, = 'utf-8') as file:
        print(file.read(), end="")
