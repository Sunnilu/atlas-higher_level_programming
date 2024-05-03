#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:  # Check if the character is lowercase
            i = chr(ord(i) - 32)  # Convert lowercase to uppercase by subtracting 32 from the ASCII value
        print("{}".format(i), end="")
    print()  # Print a newline after processing the entire string


