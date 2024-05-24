#!/usr/bin/python3
'''method for base class'''


class Base:
    '''a representation of base OOP hierachy'''
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
    else:
        __nb_objects += 1
        self.id = Base.__nb_objects

