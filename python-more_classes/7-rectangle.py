#!/usr/bin/python3
'''module for Rectangle class'''

class Rectangle:
    '''This class defines a simple rectangle'''

    number_of_instances = 0
    '''int: the number of active instances.'''

    def __init__(self, width=0, height=0, print_symbol='#'):
        '''Constructor.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            print_symbol: Symbol to represent the rectangle.
        '''
        self.width = width
        self.height = height
        self.print_symbol = print_symbol
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Property for the width of the rectangle.'''
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
        '''Property for the height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        '''Returns a formal string representation.'''
        return ((str(self.print_symbol) * self.width + "\n") * self.height)[:-1]

    def __del__(self):
        '''Called at instance deletion'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


# Create an instance
my_rectangle_1 = Rectangle(8, 4, '#')

# Print its string representation
print(my_rectangle_1)

# Delete the instance
my_rectangle_1.__del__()





