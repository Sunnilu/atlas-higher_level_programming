#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, (list, set, tuple)):
            for v in value:
                try:
                    print("{:d}".format(v))
                    return True
                except ValueError:
                    continue
        else:
            print("{d:}".format(value))
            return True
        except TypeError:
            return False
