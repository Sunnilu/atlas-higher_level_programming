#!/usr/bin/python3
    # Corrected approach to meet the task requirements
for i in range(99):  # Loop from 0 to 98
    print("{}, {}".format(i, hex(i)[2:].zfill(2)), end=', ')  # Corrected zfill to 2 for hexadecimal representation
print("99")  # Print the number 99 in decimal

