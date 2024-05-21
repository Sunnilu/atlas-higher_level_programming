#!/usr/bin/python3
''' module to add'''

import sys
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file


def main():
    # Initialize an empty list to store the arguments
    args_list = []
    
    # Iterate over the command-line arguments starting from index 1 (0 is the script name)
    for arg in sys.argv[1:]:
        # Add each argument to the list
        args_list.append(arg)
    
    # Use the save_to_json_file function to save the list to a file
    save_to_json_file(args_list, "add_item.json")

if __name__ == "__main__":
    main()

