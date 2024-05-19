#!usr/bin/python3
'''a module that defines inherits from'''

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False.

    Args:
    obj: Any Python object.
    a_class: A Python class.

    Returns:
    True if obj is an instance of a class that inherited (directly or indirectly) from a_class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

