# 0x08. Making Change

---

## Concepts

### Greedy Algorithms
- Understanding how greedy algorithms work and why they are suitable for some coin change problems.
- Recognizing scenarios where greedy algorithms might not provide the optimal solution.

### Dynamic Programming
- Using dynamic programming to solve optimization problems like the coin change problem.
- Identifying overlapping subproblems and optimal substructure in the context of this problem.

### Algorithmic Complexity
- Analyzing the time and space complexity of different approaches.
- Striving for solutions with lower complexity to ensure efficiency.

### Problem-Solving Strategies
- Breaking down the problem into smaller subproblems.
- Comparing iterative and recursive approaches to dynamic programming.

### Python Programming
- Manipulating lists and using list comprehensions.
- Implementing functions with efficient looping and conditional statements.

---
## Tasks

| Task # | Filename                | Description                                                                                      |
|--------|--------------------------|--------------------------------------------------------------------------------------------------|
| 0      | [0-making_change.py](./0-making_change.py) | Implement a function to determine the fewest coins needed to meet a given total or return `-1`. |

---

## Task Details

### 0. Change comes from within

**Filename:** [0-making_change.py](./0-making_change.py)  

**Prototype:**  
```python
def makeChange(coins, total)
```

## Description:
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given total.

- If the total is `0` or less, return `0`.
If the total cannot be met by any number of coins, return `-1`.

## Example Usage:
```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Constraints:
- Coins are represented as a list of integers, each greater than 0.
- Assume an infinite supply of each coin denomination.

## Example File:
```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
```
---
## Resources:
- **Python Official Documentation:**
    - [More Control Flow Tools (for loops, if statements)](https://docs.python.org/3/tutorial/controlflow.html)

- **GeeksforGeeks Articles:**
    - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
    - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

- **YouTube Tutorials:**
    - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jgiZlGzXMBw) for a visual and step-by-step explanation of the dynamic programming approach.
