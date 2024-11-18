# 0x07. Rotate 2D Matrix

## Overview

This project focuses on implementing an algorithm to rotate a 2D matrix by 90 degrees clockwise **in-place** using Python. It is designed to strengthen your understanding of matrix manipulation, in-place operations, and algorithm optimization.

---

## Concepts

### Matrix Representation in Python
- A 2D matrix in Python is represented as a list of lists.
- Elements are accessed and modified using nested indexing.

### In-Place Operations
- Operations are performed directly on the data structure without creating a copy.
- Helps minimize space complexity.

### Matrix Transposition
- Swapping rows with columns to transform a matrix.
- This is a key step in rotating a matrix.

### Reversing Rows
- To complete the 90-degree clockwise rotation, each row of the transposed matrix is reversed.

### Nested Loops
- Used to iterate through 2D matrices for element-wise operations.

---

## Resources
- **Python Official Documentation:**
    - [Data Structures (list comprehensions, nested list comprehension)](https://docs.python.org/3/tutorial/datastructures.html)
    - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

- **GeeksforGeeks Articles:**
    - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
    - [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

- **TutorialsPoint:**
    - [Python List](https://www.tutorialspoint.com/python/python_lists.htm) for basics of list manipulation in Python.
---

---
## Task

### 0. Rotate 2D Matrix (Mandatory)

**Filename**: `0-rotate_2d_matrix.py`

**Prototype**:
```python
def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in-place.
    """
```
