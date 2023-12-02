#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix or matrix == []:
        print()
        return
    for row in matrix:
        for integer in row:
            if integer != row[len(row) - 1]:
                print("{:d} ".format(integer), end="")
            else:
                print("{:d}".format(integer))
