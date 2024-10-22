# 0x03. Log Parsing

## Overview
The **"0x03. Log Parsing"** project is designed to help you develop Python programming skills focused on real-time data processing. You will write a script that parses logs, computes metrics like file size and the frequency of status codes, and handles data streams efficiently.

### Concepts and Resources:
To successfully complete this project, you need to be familiar with the following concepts:

#### 1. File I/O in Python:
- Learn how to read from `sys.stdin` line by line.
- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

#### 2. Signal Handling in Python:
- Handle keyboard interruptions (CTRL + C) gracefully in Python.
- [Python Signal Handling](https://docs.python.org/3/library/signal.html)

#### 3. Data Processing:
- Understand how to parse strings and extract data points such as IP addresses, status codes, and file sizes.
- Compute aggregated data, such as the total file size.

#### 4. Regular Expressions:
- Use regular expressions to validate log entry formats.
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)

#### 5. Dictionaries in Python:
- Use dictionaries to count occurrences of status codes and accumulate file sizes.
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

#### 6. Exception Handling:
- Handle potential exceptions during file reading and processing.
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

By reviewing these concepts and the associated resources, you will be prepared to handle the log parsing project, which involves parsing data from logs and computing key metrics.

## Tasks

### 0. Log parsing

**Task Description**:  
Write a script that reads from stdin line by line and computes metrics based on the input data.

**Input Format**:
```bash
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

If the format does not match, skip that line.

**Required Outputs:**
After every 10 lines or upon a keyboard interruption (CTRL + C), print the following:
Total file size: Sum of all the file sizes processed so far.
Status code occurrences: Print the number of occurrences for each of the status codes in ascending order.  

*Status codes:*
`200`, `301`, `400`, `401`, `403`, `404`, `405`, `500`

**Example:**
```bash
rofeeq@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```
