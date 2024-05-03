#!/usr/bin/python3
# Generate all possible sums of pairs of numbers from 1 to 9
sums = [i + j for i in range(1, 10) for j in range(i+1, 10)]

# Sort the sums in ascending order
sums.sort()

# Print the sorted sums in the specified format
for sum_ij in sums:
    print("{:02d}".format(sum_ij), end=", " if sum_ij!= 89 else "\n")



