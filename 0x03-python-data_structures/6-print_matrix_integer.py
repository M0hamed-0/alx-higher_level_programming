#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = 0
    while x < len(matrix):
        y = 0
        while y < len(matrix[x]):
            if y != 0:
                print(" ", end='')
            print("{:d}".format(matrix[x][y]), end='')
            y += 1
        x += 1
        print()
