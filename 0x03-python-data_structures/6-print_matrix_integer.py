#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_idx, num in enumerate(row):
            if col_idx != 0:
                print(" ", end="")
            print("{:d}".format(num), end="")
        print()
