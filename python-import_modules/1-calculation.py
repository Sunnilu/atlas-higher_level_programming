#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    a = 10
    b = 5
    addition_result = add(a, b)
    subtraction_result = subtract(a, b)
    multiplication_result = multiply(a, b)
    division_result = divide(a, b)

    print("10 + 5 = {}".format(addition_result))
    print("10 - 5 = {}".format(subtraction_result))
    print("10 * 5 = {}".format(multiplication_result))
    print("10 / 5 = {}".format(division_result))

