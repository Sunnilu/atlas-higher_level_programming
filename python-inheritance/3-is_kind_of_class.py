#!/usr/bin/python3
'''a module that defines a kind of class'''


def is_kind_of_class(obj, a_class):
    """
    check if obj is an instance of a_class or a subclass thereof.

   Args:
   obj: any python object
   a_class: a python class

   Returns: 
   true is the object is an instance of a_class or it's subclass; otherwise false
   """

   return isinstance(obj, a_class)
   

    

   