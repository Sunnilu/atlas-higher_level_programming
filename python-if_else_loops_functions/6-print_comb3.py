#!/usr/bin/python3
for i in range(1, 10):
    for j in range(i+1, 10):
        sum_ij = i + j
        print("{:02d}".format(sum_ij), end=", " if sum_ij!= 89 else "\n")


