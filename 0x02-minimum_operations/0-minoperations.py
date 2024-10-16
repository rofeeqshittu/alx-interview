#!/usr/bin/python3
""" Minimum operations challenge..."""


def minOperations(n):
    """
    Calculates the minimum number of operations to get exactly n 'H' character

    Paramaters:
    n (int): The target of 'H' characters.

    Returns:
    int: The minimum number of operations or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:  # Check if factor is a divisor of n
            operations += factor  # Count the operations
            n //= factor  # Reduce n (floor operation)
        else:
            factor += 1  # Move to the  next factor

    return operations
