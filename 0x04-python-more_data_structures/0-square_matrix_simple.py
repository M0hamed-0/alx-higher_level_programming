#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rows in range(len(matrix)):
        new_list = []
        for v in range(len(matrix[rows])):
            new_list.append(matrix[rows][v] ** 2)
        new_matrix.append(new_list)
    return (new_matrix)
