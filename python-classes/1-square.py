#!/usr/bin/python3
''' define a class square. '''
class Square:
    ''' 
    This class represents a square.

    attributes:
         _size (int): the size of the square's side.
    '''

    def __init__(self, size):
       '''
       initialize a new square object.

       parameters:
         _size (int): the size of the square's side.
       '''
       self.__size = size

    def get_size(self):
        '''
        get the size of the square.

        returns:
            int: the size of the square's side.
        '''

        return self.__size    

    def set_size(self, new_size):
        '''
        set the size of the square.

        Parameters:
            new_size (int): the new size for the square's side.
        Raises:
            ValueError: if the new size is not a positive integer.
        '''
        if isinstance(new_size, int) and new_size > 0:
            self.__size=new_size
        else:
            raise ValueError("Error: size must be a positive integer.")
        if new_size > 0:
            self.__size = new_size
        else:
            print("Error: size must be a positive integer.")

    def area(self):
        '''
        calculate the area of the square.

        returns:
            int: the area of the square.
        '''
        return self.__size ** 2

test:
mysquare=Square(3)
print(type(mysquare))#output: <class'__main__Square'>


    
