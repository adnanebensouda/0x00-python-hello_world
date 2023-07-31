#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all element of a matrix.

    Args:
        matrix (list): A list of lists of int or float.
        div (int/float): The div.
    Raises:
        TypeError: If the matrix contain non-numbers.
        TypeError: If the matrix contain rows of different size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(ro, list) for ro in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for ro in matrix for num in ro])):
        raise TypeError("matrix must be matrix (list of lists) of "
                        "integers/floats")

    if not all(len(ro) == len(matrix[0]) for ro in matrix):
        raise TypeError("Each ro of the matrix must have same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), ro)) for ro in matrix])
