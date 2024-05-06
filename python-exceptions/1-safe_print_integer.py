#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, (list, set, tuple)):
            for v in value:
                try:
                    print("{:d}".format(v))
                except ValueError:
                    continue
            return True
        elif isinstance(value,int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except TypeError:
        return False

