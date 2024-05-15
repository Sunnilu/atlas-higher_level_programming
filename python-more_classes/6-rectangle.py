#!/usr/bin/python3
'''3-rectangle: class Rectangle
'''

class Rectangle:
    '''Represents a rectangle with specified width and height'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Initializes the rectangle'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        '''Prints a string when an instance has been deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        '''Getter for the private instance attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for the private instance attribute width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter for the private instance attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for the private instance attribute height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


