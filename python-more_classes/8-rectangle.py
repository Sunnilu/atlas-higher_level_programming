#!/usr/bin/python3
'''module defines a rectangle
'''

class Rectangle:
    """
    Represents a rectangle with properties such as width, height, and methods to calculate area and perimeter.

    Attributes:
        __width (int): Private instance attribute representing the width of the rectangle.
        __height (int): Private instance attribute representing the height of the rectangle.
        number_of_instances (int): Public class attribute to keep track of the total number of Rectangle instances.
        print_symbol (str): Public class attribute defining the symbol used for string representation.

    Methods:
        __init__(self, width=0, height=0): Initializes a new Rectangle instance with given width and height.
        width(self): Property getter for width.
        width(self, value): Property setter for width, validates input.
        height(self): Property getter for height.
        height(self, value): Property setter for height, validates input.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle for printing.
        __repr__(self): Returns a string suitable for recreating the rectangle instance.
        __del__(self): Handles the destruction of the rectangle instance, decrementing the count of instances.
        bigger_or_equal(cls, rect_1, rect_2): Static method that compares two rectangles based on their areas and returns the one with the larger area or the same area if they are equal.
    """

    # Public class attribute
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with given width and height.

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle, validating the input.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle, validating the input.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: Perimeter of the rectangle. Returns 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle for printing.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return self.print_symbol * self.__width + "\n" + self.print_symbol * self.__height

    def __repr__(self):
        """
        Returns a string suitable for recreating the rectangle instance.

        Returns:
            str: String representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Handles the destruction of the rectangle instance, decrementing the count of instances.

        Prints:
            str: "Bye rectangle..." message.
        """
        print(f"Bye rectangle...{3 * '.'}")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        """
        Compares two rectangles based on their areas and returns the one with the larger area or the same area if they are equal.

        Args:
            rect_1 (Rectangle): First rectangle instance.
            rect_2 (Rectangle): Second rectangle instance.

        Returns:
            Rectangle: The rectangle with the larger area or the same area if they are equal.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle) or not isinstance(rect_2, Rectangle):
            raise TypeError("Both arguments must be instances of Rectangle.")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

