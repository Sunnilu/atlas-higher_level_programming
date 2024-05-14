#!/usr/bin/python3
'''3-rectangle: class Rectangle
'''


class Rectangle:
    '''

    Represents a rectangle with specified width and height.

    Attributes:
         _width: (int): the width of the rectangle.
         _height: (int): the height of the rectangle.

    Methods:
        width: property to get the width of the retangle.
        width(value): property setter to set the width of the rectangle.
        height: property to get the height of the rectangle.
        height(value): property setter to set the height of the rectangle.
    '''

    _width = None
    _height = None
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        return "\n".join(["#" * self._width] * self._height)

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

# Example usage
my_rectangle = Rectangle(2, 4)
print(my_rectangle)
print(f"Area: {my_rectangle.area()} - Perimeter: {my_rectangle.perimeter()}")
