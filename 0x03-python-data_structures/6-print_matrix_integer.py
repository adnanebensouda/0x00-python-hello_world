#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ro in matrix:
        for co in ro:
            print("{:d}".format(co), end=" " if co != ro[-1] else "")
        print()
