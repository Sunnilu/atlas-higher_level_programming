#!/usr/bin/python3
"""modue for lookup method"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
    obj: any python object

    returns:
    a list of strings containing the names of attributes and methods of the object"""

    return dir(obj)


