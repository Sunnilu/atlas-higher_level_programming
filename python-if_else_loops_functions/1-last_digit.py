#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

# Adjust the condition based on whether the number is negative
if number < 0:
    condition = "less than 6 and not 0"
else:
    condition = "greater than 5" if last_digit > 5 else "0" if last_digit == 0 else "less than 6 and not 0"

output = f"Last digit of {number} is {last_digit} {condition}"

print(output)


