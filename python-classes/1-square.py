#!/usr/bin/python3
class Square:
    ''' this module defines a square class for representing a square shape.
    attributes: _size (int): the size of the square's size '''
    def __init__(self, size):
       ''' initialize a new square object
       parameters:
       _size (int): the size of the square's side. '''
       self._size = size
    def area(self):
        return self.__size ** 2
