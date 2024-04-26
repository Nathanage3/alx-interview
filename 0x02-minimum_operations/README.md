# Minimum Operations

## Description

This project contains a Python method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in a text file. The text editor can execute only two operations in this file: Copy All and Paste.

## Method Prototype

```python
def minOperations(n)

Returns an integer
If n is impossible to achieve, return 0
Example
For n = 9,

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

Usage
nathan@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

nathan@ubuntu:~/0x02-minoperations$
nathan@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
nathan@ubuntu:~/0x02-minoperations$

License
This project is licensed under the terms of the MIT license.

Please replace the `License` section with your actual license. This is just a placeholder.
```
