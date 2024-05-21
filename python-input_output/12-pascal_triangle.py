#!/usr/bin/python3
'''returns a list of list'''


def pascal_triangle(n):
    """
    generate Pascal's triangle up to the nth row.

    Parameters:
    - n (int): number of rows to generate.

    Returns:
    - list of lists of integers: a list Pascal's triange up to nth row.

    Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triange.append(row)

    return triangle

