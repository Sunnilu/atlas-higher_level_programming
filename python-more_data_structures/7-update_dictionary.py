#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
 sorted_keys = sorted(a_dictionary.keys())
        for key in sorted_keys:
            print("{}: {}".format(key, a_dictionary[key]))
