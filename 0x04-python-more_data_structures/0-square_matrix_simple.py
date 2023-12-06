#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix using list comprehensions
    result_matrix = [[element ** 2 for element in row] for row in matrix]

    return result_matrix
