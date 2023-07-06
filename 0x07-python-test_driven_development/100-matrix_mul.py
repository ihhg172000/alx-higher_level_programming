#!/usr/bin/python3
"""
Contains the definition of 'matrix_mul' function.
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    for row in m_a:
        if not all(isinstance(e, (int, float)) for e in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(e, (int, float)) for e in row):
            raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    a_rows = len(m_a)
    a_cols = len(m_a[0])
    b_rows = len(m_b)
    b_cols = len(m_b[0])

    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = []
    for row in range(a_rows):
        res_row = []
        for col in range(b_cols):
            res = 0
            for r in range(b_rows):
                res += m_a[row][r] * m_b[r][col]
            res_row.append(res)
        matrix.append(res_row)
    return matrix
