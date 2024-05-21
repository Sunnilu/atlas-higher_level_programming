#!/usr/bin/python3
'''defines a student'''


class Student:
    '''
    defines a student by first_name, last_name, and age.
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Initializes a Studen instance with first_name, last_name, and age.

        Args:
            first_name (str): the first name of the student
            last_name(str): the last name of the student
            age (int): the age of the student
        '''
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
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary containing attribute names and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)


