#!/usr/bin/python3
'''defines a student'''

class Student:
    '''defines a student by first and last name and age'''

def __init__(self, first_name, last_name, age):
    '''initializes  a student instances  by name and age using json.

     Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve. Defaults to None.

        Returns:
            dict: A dictionary representation of the Student instance.
        '''
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}


