#!/usr/bin/python3
"""
    Module to determine the minimum no of coins needed to make a given amount
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determines the fewest number of coins needed to meet a given amount.

    Args:
        coins (List[int]): List of the values of coins available.
        total (int): The total amount to be made.

    Returns:
        int: Minimum number of coins needed, or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0  # Count of coins used
    for coin in coins:
        if total <= 0:
            break
        # Use as many of this coin as possible
        count += total // coin
        total %= coin

    # If total is not zero, it's not possible to form it with given coins
    return count if total == 0 else -1
