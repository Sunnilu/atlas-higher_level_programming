#!/usr/bin/python3
def print_last_digit(number):
    # Ensure the number is positive for easier calculation
    number = abs(number)
    
    # Find the last digit of the number
    last_digit = number % 10
    
    # Print the last digit without a newline
    print(last_digit, end='')
    
    # Return the absolute value of the last digit
    return abs(last_digit)