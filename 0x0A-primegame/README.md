# 0x0A. Prime Game

## Overview
The **Prime Game** is a competitive programming project that challenges you to apply concepts of prime numbers, game theory, and algorithm optimization. Maria and Ben take turns choosing prime numbers from a set of integers and removing those primes and their multiples. The player unable to make a move loses the game. The goal is to determine the overall winner after multiple rounds, assuming both players use optimal strategies.

This project reinforces understanding of efficient algorithms for prime number identification, dynamic programming, and strategic decision-making in competitive games.

---

## Concepts

### Prime Numbers
- Understanding the definition and properties of prime numbers.
- Developing efficient algorithms for finding prime numbers in a range.

### Sieve of Eratosthenes
- An optimized algorithm for identifying all prime numbers up to a given limit.

### Game Theory
- Principles of turn-based games, optimal play, and winning strategies.

### Dynamic Programming / Memoization
- Reusing previously computed results to optimize calculations for multiple game rounds.

### Python Programming
- Loops and conditionals to implement game logic.
- Lists and arrays for tracking game state and removed numbers.

---

## Tasks

| Task   | File                                            | Description                                                                                       |
|--------|-------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 0      | [0-prime_game.py](./0-prime_game.py)            | Implement a function `def isWinner(x, nums)` to determine the winner of the prime game.          |

---
---

## Example Usage

```python
#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

## Output:
```bash
Winner: Ben
```

## Resources

### Prime Numbers and Sieve of Eratosthenes
- **[Khan Academy: Prime Numbers](https://www.khanacademy.org/math/cc-fourth-grade-math/imp-factors-multiples-and-patterns/imp-prime-and-composite-numbers/v/prime-numbers):** Introduction to prime numbers.
- **[Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/):** Step-by-step guide to implementing the algorithm in Python.

### Game Theory Basics
- **[Game Theory Introduction](https://www.investopedia.com/terms/g/gametheory.asp):** Explanation of game theory and strategic decision-making.

### Dynamic Programming
- **[What Is Dynamic Programming](https://skerritt.blog/dynamic-programming/):** Introduction and Python examples.

### Python Documentation
- **[Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists):* Guide to managing lists in Python.

---
---

## Repository Information

- **GitHub Repository:** [alx-interview](https://github.com/rofeeqshittu/alx-interview)
- **Directory:** `0x0A-primegame`
- **File:** `0-prime_game.py`

---

## Additional Notes

- **Assumptions:**
  - `n` and `x` will not exceed 10,000.
  - The game starts with Maria taking the first turn.
  - Both players play optimally.
- **Constraints:**
  - No libraries or packages can be imported.
---
---
