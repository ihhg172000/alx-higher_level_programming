#!/usr/bin/python3
"""Contains the definition of 'pascal_triangle' function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for r in range(n - 1):
        row = [1]
        for c in range(r + 1):
            if c != r:
                row.append(triangle[r][c] + triangle[r][c + 1])
        row.append(1)
        triangle.append(row)
    return triangle
