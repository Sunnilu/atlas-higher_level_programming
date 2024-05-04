#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub as add, add as sub, div as mul, mul as div
    a = 10
    b = 5
    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)
    print("10 + 5 = {}".format(addition_result))
    print("10 - 5 = {}".format(subtraction_result))
    print("10 * 5 = {}".format(multiplication_result))
    print("10 / 5 = {}".format(division_result))



