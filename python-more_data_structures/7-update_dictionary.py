#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

# Example usage:
my_dict = {'a': 1, 'b': 2}
update_dictionary(my_dict, 'c', 3)  # Adds a new key-value pair
update_dictionary(my_dict, 'a', 10) # Updates the value of an existing key
print(my_dict)  # Output: {'a': 10, 'b': 2, 'c': 3}


