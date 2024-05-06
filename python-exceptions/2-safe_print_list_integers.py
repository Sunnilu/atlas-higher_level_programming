#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for _ in my_list:
        count += 1
    for item in my_list:
        try:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                count -= 1
                if count == 0:
                    break
        except TypeError:
            pass
    return count





