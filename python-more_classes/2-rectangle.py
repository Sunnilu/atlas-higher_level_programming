#!usr/bin/python3
'''2-rectangle: class Rectangle
'''

class Rectangle:
    '''

    Represents a rectangle with specified width and height.

    Attributes:
        _width (int): the width of the rectangle.
        _height (int): the height of the rectangle.

    Methods:
        width: Property to get the width of the rectangle.
        width(value): property setter to set the width of the rectangle
        height: property to get the height of the rectangle.
        height(value): property setter to set the height of the rectangle.
    '''

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance with optional width and height."""
        if not isinstance(width, int) or width < 0:
            raise ValueError("width must be an integer >= 0")
        if not isinstance(height, int) or height < 0:
            raise ValueError("height must be an integer >= 0")
        self._width = width
        self._height = height

    @property
    def width(self):
        """Property to retrieve the width."""
        return self._width

    @width.setter
    def width(self, value):
        """Property setter to set the width.

        Args:
            value (int): The new width.

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
        """Property to retrieve the height."""
        return self._height

    @height.setter
    def height(self, value):
        """Property setter to set the height.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Public instance method to calculate and return the rectangle's area."""
        return self._width * self._height

    def perimeter(self):
        """Public instance method to calculate and return the rectangle's perimeter.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    