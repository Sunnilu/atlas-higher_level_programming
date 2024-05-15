#!/usr/bin/python3
"""Module to find the max integer in a vector
"""


def max_integer(list=[]):
    '''function to find and return the max integer in a list of interers, if the list is 
    empty, the function returns none
    '''
    
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
