#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# calculate the last digit
last_digit = abs(number) % 10
output = f"last digit of {number} is {last_digit}"
if last_digit > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    output += "and is 0"
elif last_digit < 6 and last_digit != 0:
    output += "and is less than 6 and not 0"

    print(output)
