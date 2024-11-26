# 0x08. Making Change

## Requirements

- Each file should end with a new line.
- All files must be executable.
- A `README.md` file is mandatory in the root directory.

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
