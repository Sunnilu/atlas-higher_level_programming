#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):  # Adjusted to iterate up to x
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
                if count == x:
                    break
        except IndexError:
            # This block is intentionally left empty because we're not supposed to handle non-integer values explicitly
            pass
    return count







