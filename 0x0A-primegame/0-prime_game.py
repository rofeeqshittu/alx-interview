#!/usr/bin/python3
"""
    Prime game module.
"""


def isWinner(x, nums):
    """
    Module to get the winner of the prime game question.
    """

    # Step 1:  Find the largest number in the game
    max_num = max(nums)

    # Step 2: Precompute primeNo up to max_num using the Sieve of Eratosthenes
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 & 1 are Not primes

    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Step 3: Count primes up to each no
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Step 4: Simulate each game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 5: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
