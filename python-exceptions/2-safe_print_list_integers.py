#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # Initialize a counter for the number of integers printed
    count = 0
    
    # Iterate through the list up to x elements
    for i in range(min(x, len(my_list))):
        try:
            # Check if the current element is an integer
            if isinstance(my_list[i], int):
                # Print the integer using the specified format
                print("{:d}".format(my_list[i]), end="")
                # Increment the counter
                count += 1
        except IndexError:
            # This exception is caught if x is greater than the length of my_list
            break
    
    # Print a newline character at the end
    print()
    
    # Return the number of integers printed
    return count

# Example usage
my_list = [1, "two", 3, 4.5, "five", 6]
x = 3
print(safe_print_list_integers(my_list, x))











