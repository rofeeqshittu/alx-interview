#!/usr/bin/python3
"""
    Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid: A 2D list representing the map, where
             0 = water and 1 = land.

    Returns:
        int: The total perimeter of the island.
    """
    # Initialize perimeter counter
    perimeter = 0

    # Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # Loop through every cell in the grid
    for row in range(rows):
        for col in range(cols):
            # If the cell is land, add 4 to the perimeter
            if grid[row][col] == 1:
                perimeter += 4

                # Check if there's land above: substract 2 if so
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # Check if there's land to the left; substract 2 if so
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
