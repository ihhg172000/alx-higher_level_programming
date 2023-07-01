#!/usr/bin/python3
"""
Contains the definition of 'matrix_divided' function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A matrix of integers or floats.
        div (int or float): The divisor of all elements.

    Returns:
        list: A new matrix.

    Raises:
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is equal to 0
        TypeError: If one row not the same size as other rows.
        TypeError: If the matrix contains element not integer nor float.
    """
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for idx in range(len(matrix)):
        if idx > 0 and len(matrix[idx]) != len(matrix[idx - 1]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for number in matrix[idx]:
            if (
                not isinstance(number, (int, float)) or
                isinstance(number, bool)
            ):
                raise TypeError(
                                "matrix must be a matrix (list of lists) " +
                                "of integers/floats"
                                )
            new_row.append(round((number / div), 2))
        new_matrix.append(new_row)
    return new_matrix
