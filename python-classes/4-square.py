#!/usr/bin/python3
''' defines a class square '''

class Square:
    ''' defines a square. '''

    def __init__(self, size = 0):
        ''' constructor.
        Args:
            size: length of a side of the square.
        '''
        self.size = size

    @property
    def size(self):
        ''' Property for the length of a side of this square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        '''
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(Value, int):
            raise TypeError("size must be an integer")
        if value < 0):
            raised ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' Area of this square.

        Returns:
            The size squared.
            '''
        return self.__size ** 2
