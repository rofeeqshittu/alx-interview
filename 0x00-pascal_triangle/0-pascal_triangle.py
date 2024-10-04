#!/usr/bin/python3
"""
    Create a function pascal_triangle(n) that returns a list of lists of
    integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
        returns a list of lists of integers representing the
        Pascal’s triangle of n:
    """
    if n <= 0:
        return []

    # Initialize the triangle list with with the first row
    triangle = [[1]]

    # Loop to generate each row starting from the second one
    for i in range(1, n):
        row = [1]  # The first element of each row is always 1
        # Generate the element in the middle of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i-1][j])
        row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle
