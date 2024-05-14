#!/usr/bin/python3
'''1-rectangle: class Rectangle
'''

class Rectangle:
    """
    Represents a rectangle with specified width and height.

    Attributes:
        _width (int): The width of the rectangle.
        _height (int): The height of the rectangle.

    Methods:
        width: Property to get the width of the rectangle.
        width(value): Property setter to set the width of the rectangle.
        height: Property to get the height of the rectangle.
        height(value): Property setter to set the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with optional width and height.

        Parameters:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        if not isinstance(width, int) or width < 0:
            raise ValueError("width must be an integer >= 0")
        if not isinstance(height, int) or height < 0:
            raise ValueError("height must be an integer >= 0")
        self._width = width
        self._height = height

    @property
    def width(self):
        """Property to retrieve the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Property setter to set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Property to retrieve the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Property setter to set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
          raise ValueError("height must be >= 0")
        self._height = value

# Attempt to create a Rectangle instance with invalid parameters
try:
    my_rectangle = Rectangle(2, -3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))   


