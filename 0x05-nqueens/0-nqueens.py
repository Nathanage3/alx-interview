#!/usr/bin/python3
""" N queens """


import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """Find all possible positions for N queens on an NxN board.

    The positions are represented by a list of indices in the
    range [0, N) where the index represents the row and the value
    at that index represents the column.

    The positions are found by using a recursive backtracking
    algorithm. The positions are yielded from the recursive function
    as they are found.

    Parameters:
    n (int): The size of the board. Must be at least 4.
    i (int): The current row. Defaults to 0.
    a (list): The list of column indices for the queens in the
        rows above the current row. Defaults to an empty list.
    b (list): The list of column indices plus row indices for the
        queens in the rows above the current row. Defaults to an
        empty list.
    c (list): The list of column indices minus row indices for the
        queens in the rows above the current row. Defaults to an
        empty list.

    Yields:
    list: The list of column indices for the N queens.
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a
def solve(n: int) -> None:
    """Print all possible positions for N queens on an NxN board.

    The positions are represented by a list of indices in the
    range [0, N) where the index represents the row and the value
    at that index represents the column.

    Parameters:
    n (int): The size of the board. Must be at least 4.
    """
    k = []  # list to store the positions of the queens
    i = 0  # current row
    # iterate over all possible positions for the queens
    for solution in queens(n, 0):
        for s in solution:
            # add the current position to the list
            k.append([i, s])
            # increment the current row
            i += 1
        # print the positions of the queens
        print(k)
        k = []
        i = 0
solve(n)