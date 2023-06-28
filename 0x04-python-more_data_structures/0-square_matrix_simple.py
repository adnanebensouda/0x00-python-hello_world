#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda p: p * p), elim)) for elim in matrix]
