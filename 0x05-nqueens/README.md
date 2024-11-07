# 0x05. N Queens

## Overview
The **N Queens** project is a classic problem in computer science and mathematics that involves placing `N` queens on an `N×N` chessboard so that no two queens can attack each other. This project applies backtracking algorithms to explore possible solutions, utilizing recursive functions and list manipulations. Solving the N Queens problem reinforces understanding of algorithmic thinking, optimization techniques, and handling command-line arguments in Python.

## Concepts
The following concepts are essential to implementing the solution:

1. **Backtracking Algorithms**  
   Explore potential solutions by placing queens in all rows and backtrack when conflicts occur.  
   - *Resource*: [Introduction to Backtracking Algorithms](https://www.geeksforgeeks.org/introduction-to-backtracking-2/)

2. **Recursion**  
   Implement recursive functions to achieve backtracking.  
   - *Resource*: [Recursion in Python](https://realpython.com/python-thinking-recursively/)

3. **List Manipulations in Python**  
   Use lists to manage the placement of queens.  
   - *Resource*: [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

4. **Python Command Line Arguments**  
   Handle command-line arguments using the `sys` module.  
   - *Resource*: [Command Line Arguments in Python](https://docs.python.org/3.3/library/sys.html#sys.argv)

## Additional Resources
- [Mock Interview](https://www.youtube.com/watch?v=GneS80iYa7I)

### Read on:
- [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29)
- [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

## Tasks

| Task No. | Filename      | Description                                                                                                        |
|----------|---------------|--------------------------------------------------------------------------------------------------------------------|
| 0        | `0-nqueens.py` | Implements the N Queens solution, displaying all valid board configurations where queens are non-attacking. |

## 0. N Queens

The goal is to create a program that solves the N Queens problem for any `N ≥ 4`. If the program encounters invalid input, it will return appropriate error messages.

### Usage
Run the program as follows:
```bash
./0-nqueens.py N
```

Where:

N must be an integer ≥ 4.
Each solution is displayed on a new line, formatted as a list of [row, column] positions.

### Error Handling
1. If the program is called with the wrong number of arguments:
bash
```bash
Usage: nqueens N
```

2. If `N` is not an integer:
```bash
N must be a number
```

3. If `N` is less than 4:
```bash
N must be at least 4
```

### Example Output
For `N=4`, the program should output:
```bash
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

### Example Commands
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
...
```
