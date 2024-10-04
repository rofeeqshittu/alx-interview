# 0x01. Lockboxes

## Overview
This project explores an algorithmic solution to determine whether all boxes in a sequence can be unlocked. The boxes are numbered sequentially, and each box may contain keys to other boxes. You need to implement a function to figure out if all the boxes can be opened.

## Concepts
- **Lists and List Manipulation**: Understand how to iterate and manage lists in Python. [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

- **Graph Theory Basics**: Applying graph traversal algorithms (Depth-First Search or Breadth-First Search) can be beneficial in this context. [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)

- **Algorithmic Complexity**: Optimizing the performance of your solution, particularly in time and space complexity, is key. [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)

- **Recursion**: Some implementations may involve recursive traversal through the boxes. [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

- **Queue and Stack**: Use of data structures like queues and stacks to traverse through the boxes and keys. [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

- **Set Operations**: Sets can be used to keep track of visited boxes or collected keys. [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Tasks

### 0. Lockboxes
**Filename**: [`0-lockboxes.py`](./0-lockboxes.py)  
This task implements a function `canUnlockAll(boxes)` that checks if all the boxes can be unlocked.  
- **Input**: A list of lists, where each list represents a box containing keys to other boxes.
- **Output**: Returns `True` if all boxes can be unlocked, otherwise `False`.

## Example

```bash
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
carrie@ubuntu:~/0x01-lockboxes$

