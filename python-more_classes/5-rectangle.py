#!/usr/bin/python3
'''5-rectangle: class Rectangle
'''

class Rectangle:
    '''

    Represents a rectangle with specified width and height.

    Attributes:
         _width (int): the width of the rectangle.
         _height (int): the height of the rectangle.

    Methods:
        width: property to get the width of the rectangle.
        width(value): property setter to set the width of the rectangle.
        height: property to get the height of the rectangle.
        height(value): property setter to set the height of the rectangle.
    '''

    
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

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
        print("Bye rectangle...")

# Ensure my_rectangle is defined before any operation or print statement that uses it
my_rectangle = Rectangle(2, 4)

# Calculate and print the area and perimeter
print(f"Area: {my_rectangle.area()} - Perimeter: {my_rectangle.perimeter()}")

# The __del__ method will be called automatically when my_rectangle goes out of scope
# or when the program ends, printing "Bye rectangle..."

