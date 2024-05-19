#!/usr/bin/python3
'''module to define same class'''


def is_same_class(obj, a_class):

    '''return true if the object is exactly an instance of the specified class, otherwise return false

    Args:
    obj: A python object
    a_class: A Python class

    Returns:
    return true if object is an instance of a class, otherwise return false
    '''

    return type(obj) is a_class
