#!/usr/bin/python3
# Import specific functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Define variables a and b
a = 10
b = 5

# Call and print the results of the imported functions
result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

# Print the results, adhering to the constraint of using print no more than 4 times
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")




