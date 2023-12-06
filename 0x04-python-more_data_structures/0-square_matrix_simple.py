#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    delta_matrix = []
    for row in matrix:
        lst = []
        for elem in row:
            lst.append(elem ** 2)
        delta_matrix.append(lst)
    return (delta_matrix)
