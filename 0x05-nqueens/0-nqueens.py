#!/usr/bin/python3
"""
    Solves the N queens puzzle by placing N non-attacking queens
    on an N×N board.
    """
import sys


def print_solution(positions):
    """Print the positions of queens in a solution format."""
    solution = []
    for row, col in enumerate(positions):
        solution.append([row, col])
    print(solution)


def is_safe(positions, row, col):
    """Check if placing a queen at row, col is safe from attacks."""
    for r, c in enumerate(positions[:row]):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, positions):
    """Recursive backtracking function to place queens on the board."""
    if row == n:
        print_solution(positions)
        return
    for col in range(n):
        if is_safe(positions, row, col):
            positions[row] = col
            solve_nqueens(n, row + 1, positions)


def main():
    """
    Main entry point to handle command-line argument
    and solve puzzle.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    positions = [-1] * n
    solve_nqueens(n, 0, positions)


if __name__ == "__main__":
    main()
