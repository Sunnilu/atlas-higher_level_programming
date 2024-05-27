#!/usr/bin/python3
'''Module for rectangle class'''


class Rectangle:
    '''
    Class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    '''

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        
        Args:
            value (int): New width value.
        """
        if isinstance(value, int) and value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive integer.")

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        
        Args:
            value (int): New height value.
        """
        if isinstance(value, int) and value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive integer.")

    def area(self):
        """
        Calculate and return the area of the rectangle.
        
        Returns:
            int: Area of the rectangle.
        """
        return self._width * self._height

    def display(self):
        """
        Display the rectangle using asterisks (*) in the console.
        """
        for _ in range(self._height):
            print("*" * self._width)

# Example usage
r = Rectangle(12, 15)
print(f"Width: {r.width}, Height: {r.height}")
print(f"Area: {r.area()}")

try:
    r.width = 20  # Changing width
    r.display()
except Exception as e:
    print(e)