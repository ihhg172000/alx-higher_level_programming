#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for idx in range(len(list)):
            print(list[idx], end=" " if idx < len(list) - 1 else "")
        print("")
