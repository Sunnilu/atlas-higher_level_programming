#!/usr/bin/python3
'''module for a MyList class'''

class MyList(list):
    '''Custom MyList class.'''
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def print_sorted(self):
        '''Method for printing sorted list.'''
        print(sorted(self))

# Example usage:
if __name__ == "__main__":
    # Creating an instance of MyList with attributes
    my_list = MyList("example_list", "This is an example list")
    my_list.append(3)
    my_list.append(1)
    my_list.append(2)

    # Accessing attributes
    print("Name:", my_list.name)
    print("Description:", my_list.description)
    print("Sorted list:")
    my_list.print_sorted()