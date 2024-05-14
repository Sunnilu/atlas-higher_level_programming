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

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

# Example usage
if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    print(r1)
    print(f"Area: {r1.area()} - Perimeter: {r1.perimeter()}")
    r2 = Rectangle(3, 5)
    print(r2)
    print(f"Area: {r2.area()} - Perimeter: {r2.perimeter()}")

    # Deleting instances
    del r1
    del r2
    print(f"{Rectangle.number_of_instances} instances of Rectangle")
