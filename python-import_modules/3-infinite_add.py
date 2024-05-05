#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from sys import argv
    sumint = 0
    for i in range(1, len(argv)):
        sumint += int(argv[i])
    print("{}".format(sumint))

