#!/usr/bin/python3
'''module for a MyList class'''


class Mylist(list):
    '''custom Mylist class'''
    def print_sorted(self):
        '''method for printing sorted list.'''
        print(sorted(self))

