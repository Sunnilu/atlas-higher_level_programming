#!/usr/bin/python3
# Using a single loop to iterate from 0 to 98 and print both decimal and hexadecimal representations
for i in range(99):  # Loop from 0 to 98
    print("{}, {}".format(i, hex(i)[2:].zfill(2)), end=', ')  # Print decimal and hexadecimal representation
print("99")  # Print the number 99 in decimal

