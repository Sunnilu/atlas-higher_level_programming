#!/usr/bin/python3
''' Square module '''

class Square:
    ''' defines a square. '''

    def __init__(self, size = 0):
        ''' constructor.
        Args:
            size: length of a side of the square.
        '''
        self.size = size

    @property
    def dict (self):
        ''' property to access the attributes of the square as a dictionary. '''
        return {'size': self.__size}

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        '''
        return the size squared

    size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' Area of this square.

        Returns:
            the size squared.
        '''
        return self.__size ** 2
