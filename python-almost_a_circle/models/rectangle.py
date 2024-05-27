#!/usr/bin/python3
'''module for rectangle class'''
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.setter_validation("width", value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self.setter_validation("height", value)
        self._height = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self.setter_validation("x", value)
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self.setter_validation("y", value)
        self._y = value

    def area(self):
        return self._width * self._height

    def display(self):
        print("\n" * self._y, end="")
        for i in range(self._height):
            print(" " * self._x + "#" * self._width)

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        return {
            'x': getattr(self, "x"),
            'y': getattr(self, "y"),
            'id': getattr(self, "id"),
            'height': getattr(self, "height"),
            'width': getattr(self, "width")
        }

    @staticmethod
    def setter_validation(attribute, value):
        if type(value)!= int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
