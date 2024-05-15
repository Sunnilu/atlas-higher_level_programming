#!/usr/bin/python3
'''module for Rectangle class'''


class Rectangle:
    '''this class defines a simple rectangle'''

    number_of_instances = 0
    '''int: the number of active instances.'''

    print_symbol = '#'
    '''type: print symbol, can be any type.'''

    def __init__(self, width=0, height=0):
        '''constructor.

        Args:
            width: the width of rectangle.
            height: the height of rectangle.
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''property for the width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''property for the height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns area of this rectangle.'''
        return self.width * self.height

    def perimeter(self):
        '''returns perimeter of this rectangle.'''
        if not self.width or not self.height:
            return ""
        return 2 * (self.width + self.height)

    def __del__(self):
        '''called at instance deletion'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __repr__(self):
        '''returns formal string representation...'''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"


