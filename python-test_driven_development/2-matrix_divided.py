#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
It handles both integers and floats, and returns a new matrix with
result rounded to two decimal.
"""


def matrix_divided(matrix, div):
    """
Divides all elements of a matrix.

Each element in the matrix (a list of lists) is divided by div.
The result is a new matrix with the results rounded to 2 decimal places.
"""
    if (
        not isinstance(matrix, list)
        or not all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        for item in row:
            if not isinstance(item, (float, int)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                    )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return new_matrix
