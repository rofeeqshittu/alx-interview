#!/usr/bin/python3
"""
    Contains rotate_2d_matrix fuction.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (List[List[int]]): The 2d matrix to be rotated.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each for
    for row in matrix:
        row.reverse()
