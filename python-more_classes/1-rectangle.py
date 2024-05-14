#!/usr/bin/python3


@property
def height(self):
    ''' method that returns the value of the height

    Returns:
        height of the rectangle
    '''

    return self.__height

@height.setter
def height(self, value:
        '''method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
