#!/usr/bin/python3
def print_list_integer(my_LIST=[]):
    for num in my_LIST:
        print("{}".format(num))


# Example usage:
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)