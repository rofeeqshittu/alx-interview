# 0x09. Island Perimeter

## Overview
The **Island Perimeter** project involves developing a Python function to calculate the perimeter of an island in a grid. The grid is represented by a 2D list of integers, where `0` represents water and `1` represents land. The challenge is to determine the perimeter of the landmass using algorithmic and logical techniques, ensuring compliance with the specific grid constraints.

This project enhances problem-solving skills and understanding of 2D arrays, conditional logic, and Python programming.

---

## Concepts
### 2D Arrays (Matrices)
- Access and iterate over elements in a 2D list.
- Navigate through adjacent cells (horizontally and vertically).

### Conditional Logic
- Apply conditions to identify if a cell contributes to the perimeter.

### Counting Techniques
- Develop a method to count edges contributing to the perimeter.

### Problem-Solving Strategies
- Break the problem into subtasks, such as identifying land cells and calculating their contribution.

### Python Programming
- Use nested loops for grid traversal.
- Implement conditional checks for adjacent cells.

---

## Tasks

| Task   | File                                              | Description                                                                                                                                         |
|--------|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | [0-island_perimeter.py](./0-island_perimeter.py)  | Create a function `def island_perimeter(grid):` to calculate the perimeter of an island represented by `1s` in a 2D grid.                           |

---

## Requirements
- **Allowed Editors:** `vi`, `vim`, `emacs`
- **Execution Environment:** Ubuntu 20.04 LTS, Python 3.4.3
- **PEP 8 Compliance:** Version 1.7
- **File Format:**
  - First line: `#!/usr/bin/python3`
  - Ends with a newline
  - All files must be executable
- **Documentation:**
  - Modules and functions must be fully documented.

---

## Example Usage

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
```

**Output:**
```bash
12
```

---
## Resources
**Python Documentation**
- [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions): How to handle lists of lists.
**Articles**
- GeeksforGeeks: [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/): Learn to work with 2D arrays effectively.
- TutorialsPoint: [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Guide to creating and manipulating Python lists.

**Videos**
- [Python 2D Arrays and Lists](https://www.youtube.com/watch?feature=shared&v=aNzepGawwCI): Tutorials on 2D array manipulation in Python.


[*Mock Technical Interview*](https://www.youtube.com/watch?v=fFgEM6CMQc4)
 
---
---
