#!/usr/bin/python3
'''a module that defines a kind of class'''


def is_kind_of_class(obj, a_class):
    '''
    check if obj is an instance of a_class or a subclass thereof.

    Parameters:
    obj (object): the object to check.
    a_class (type): the class to compare against.

    Returns:
    bool: true if obj is an instance of a_class or a subclass thereof, false otherwise
    '''

    # get the class of the object
    obj_class = type(obj)

    #start travesing u the inheritance chain
    current_class = obj_class
    while current_class is not None:
        #check if the current cass is the target class
        if current_class is a_class:
            return True


    # if we haven't returned yet, the object isn't an instance therefore
    return False
