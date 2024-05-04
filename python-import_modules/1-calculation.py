#!/usr/bin/python3
if _name_ == "_main_":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addition_result = add(a, b)
    subtraction_result = subtract(a, b)
    multiplication_result = multiply(a, b)
    division_result = divide(a, b)

    print("10 + 5 =", addition_result)
    print("10 - 5 =", subtraction_result)
    print("10 * 5 =", multiplication_result)
    print("10 / 5 =", division_result)
