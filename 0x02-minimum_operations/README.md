# 0x02. Minimum Operations

## Overview
The **Minimum Operations** project involves developing an algorithm to calculate the minimum number of operations required to achieve a specific number of characters in a text file using only "Copy All" and "Paste" operations. This project aims to strengthen your understanding of dynamic programming and prime factorization while honing your Python programming skills.

## Concepts Needed
To effectively solve the Minimum Operations problem, it is important to understand the following concepts:

- **Dynamic Programming**: 
  - Familiarity with dynamic programming will help in breaking down the problem into simpler subproblems and building a solution iteratively.
  - [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)

- **Prime Factorization**:
  - Understanding how to perform prime factorization is crucial, as the problem can be reduced to finding the sum of the prime factors of the target number `n`.
  - [Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-factorization-prealg/v/prime-factorization)

- **Code Optimization**:
  - Approaching problems with an optimization mindset can lead to finding the most efficient solutions.
  - [How to Optimize Python Code](https://stackify.com/how-to-optimize-python-code/)

- **Greedy Algorithms**:
  - The problem can also be approached using greedy algorithms, where the best option is chosen at each step.
  - [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)

- **Basic Python Programming**:
  - Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
  - [Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

By studying these concepts and utilizing the provided resources, you will be equipped to tackle the Minimum Operations problem effectively, applying both mathematical reasoning and programming skills.

## Tasks

### 0. Minimum Operations
**Filename:** [0-minoperations.py](./0-minoperations.py)  
**Description:**  
In a text file, there is a single character 'H'. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` H characters in the file.

#### Prototype
```python
def minOperations(n):
    """
    Returns the minimum number of operations to reach n H characters.
    If n is impossible to achieve, return 0.
    """
```

Example:
```python
n = 9

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

# Number of operations: 6
```
