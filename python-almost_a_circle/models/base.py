#!/usr/bin/python3
'''module for base class'''
import json
import csv
import turtle

class Base:
    '''A representation of the base of our OOP hierarchy'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Constructor for Base class.

        Parameters:
            id (int): Identifier for the instance. If None, automatically assigned.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Convert a list of dictionaries to a JSON string.

        Parameters:
            list_dictionaries (list): List of dictionaries to be converted.

        Returns:
            str: JSON representation of the input list of dictionaries.
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return ""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Save a list of objects to a JSON file.

        Parameters:
            cls (class): The class.
            list_objs (list): List of objects to be saved.
        '''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    # Other methods...

    @staticmethod
    def draw(cls, list_rectangles, list_squares):
        '''
        Draw rectangles and squares using the turtle module.

        Parameters:
            cls (class): The class.
            list_rectangles (list): List of Rectangle objects.
            list_squares (list): List of Square objects.
        '''
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares
        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
        window.exitonclick()
