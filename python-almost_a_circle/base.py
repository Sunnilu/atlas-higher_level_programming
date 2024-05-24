#!/usr/bin/python3
'''creates a file named base'''


class Base:
    """
    Base class for managing unique IDs for objects.

    This class serves as the foundation for managing the 'id' attribute in future classes within your project.
    By utilizing this class as a base, you can avoid duplicating code for managing IDs and ensure consistency across your project.
    """

    __nb_objects = 0  # private class attribute to keep track of objects

    def __init__(self, id=None):
        """
        Initialize a Base object with a unique ID.

        Args:
            id (int, optional): The ID for the object. If not provided, a unique ID will be generated automatically.
        """
        if id is not None:
            self.id = id  # assign provided id to the object
        else:
            self.__class__.__nb_objects += 1  # increment object counter
            self.id = self.__class__.__nb_objects  # assign the new value to the object's ID
