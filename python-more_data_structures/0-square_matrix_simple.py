#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            return
        else:
            new_row = [x**2 for x in row]
            new_matrix.append(new_row)
    return new_matrix
