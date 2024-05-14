class Rectangle:
    '''A simple Rectangle class with a height property.'''
    
    def __init__(self, height=0):
        '''Initializes a new Rectangle instance with a given height.'''
        if not isinstance(height, int) or height < 0:
            raise ValueError("height must be an integer >= 0")
        self.__height = height
    
    @property
    def height(self):
        '''Method that returns the value of the height.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Method that defines the height.

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

