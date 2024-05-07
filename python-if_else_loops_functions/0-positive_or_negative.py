#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Print the number
print(number, end=" ")

# Check if the number is positive, negative, or zero and print the result
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
