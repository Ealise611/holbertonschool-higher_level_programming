#!/usr/bin/python3
"""
a function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    a function that returns a list of lists of integers
    that represents the Pascal's triangle of n
    """
    if n <= 0:
        return list()

    result = [[1]]
    for i in range(1, n):
        prev_row = result[-1]
        row = []
        row.append(1)
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        row.append(1)
        result.append(row)
    return result
