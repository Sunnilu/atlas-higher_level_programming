#!/usr/bin/env python3
"""Module for rectangle class"""

from models.base import Base

class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter."""
        return self._width

    @width.setter
    def width(self, value):
        """Width setter."""
        self.setter_validation("width", value)
        self._width = value

    @property
    def height(self):
        """Height getter."""
        return self._height

    @height.setter
    def height(self, value):
        """Height setter."""
        self.setter_validation("height", value)
        self._height = value

    @property
    def x(self):
        """X coordinate getter."""
        return self._x

    @x.setter
    def x(self, value):
        """X coordinate setter."""
        self.setter_validation("x", value)
        self._x = value

    @property
    def y(self):
        """Y coordinate getter."""
        return self._y

    @y.setter
    def y(self, value):
        """Y coordinate setter."""
        self.setter_validation("y", value)
        self._y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.height * self.width

    def display(self):
        """Display the rectangle using the console."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the rectangle attributes based on positional or keyword arguments."""
        if args:
            self.id, self.width, self.height, self.x, self.y = args
        for key, val in kwargs.items():
            setattr(self, key, val)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }

    @staticmethod
    def setter_validation(attribute, value):
        """Validate the attribute value."""
        if type(value)!= int:
            raise TypeError(f"{attribute} must be an integer")
        if attribute in ['x', 'y']:
            if value < 0:
                raise ValueError(f"{attribute} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"