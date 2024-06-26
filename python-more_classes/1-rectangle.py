#!/usr/bin/python3
'''1-rectangle: class Rectangle
'''

class Rectangle:
    """
    Represents a rectangle with specified width and height.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        width: Property to get the width of the rectangle.
        width(value): Property setter to set the width of the rectangle.
        height: Property to get the height of the rectangle.
        height(value): Property setter to set the height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        '''
        initializes the rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter for the private instance attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for the private instance attribute of width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' getter for the private instance attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for the private instance attribute height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
