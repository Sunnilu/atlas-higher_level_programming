#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        '''Initializes a new Rectangle instance with optional width and height.'''
        self._width = width
        self._height = height

    @property
    def width(self):
        '''Property to retrieve the width.'''
        return self._width

    @width.setter
    def width(self, value):
        '''Property setter to set the width.

        Args:
            value: The new width.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        '''Property to retrieve the height.'''
        return self._height

    @height.setter
    def height(self, value):
        '''Property setter to set the height.

        Args:
            value: The new height.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

