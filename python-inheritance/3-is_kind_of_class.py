#!/usr/bin/python3
'''a module that defines a kind of class'''

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.

    Args:
    obj: Any Python object.
    a_class: A Python class.

    Returns:
    True if obj is an instance of a_class or its subclass; otherwise False.
    """
    return isinstance(obj, a_class)



   
    

   