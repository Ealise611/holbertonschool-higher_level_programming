#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    return square_matrix
