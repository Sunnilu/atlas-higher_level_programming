#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then saves them to a file.
script takes command-line arguments and adds them to a list. It then
saves this list to a JSON file named add_item.json. 
"""

import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_to_list_and_save(args):
    """
    Adds the provided arguments to a list and saves it to a JSON file.

    Args:
        args (list): A list of arguments to be added to the existing list.

    Returns:
        None
    """
    try:
        # Load existing list or create a new one
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Add new items to the list
    items.extend(args)

    # Save the updated list to a JSON file
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    # Exclude script name from arguments
    args = sys.argv[1:]
    add_to_list_and_save(args)

