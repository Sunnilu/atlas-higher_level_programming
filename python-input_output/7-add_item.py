#!/usr/bin/python3
''' module to add'''

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __dict__(self):
        return {'name': self.name, 'age': self.age}

def main():
    # Check if the file exists
    file_name = 'add_item.json'
    data = []

    # If the file exists, load its content
    if path.exists(file_name):
        data = load_from_json_file(file_name)

    # Add command-line arguments to the list (excluding "Holberton")
    args = [arg for arg in sys.argv[1:] if arg != "Holberton"]
    data.extend(args)

    # Add an instance of MyClass to the list
    my_instance = MyClass("John", 30)
    data.append(my_instance.__dict__())

    # Save the list to a JSON file
    save_to_json_file(data, file_name)
    print("Items added to add_item.json:", args)

if __name__ == "__main__":
    main()


