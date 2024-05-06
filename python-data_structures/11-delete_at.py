#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is out of range or negative
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create a new list with elements before idx and after idx
    new_list = my_list[:idx] + my_list[idx+1:]

    return new_list

