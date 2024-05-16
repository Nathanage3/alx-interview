# N-Queens Puzzle Solver

The N-Queens puzzle is a classic problem in computer science and mathematics. The challenge is to place N queens on an N×N chessboard in such a way that no two queens can attack each other. This means that no two queens share the same row, column, or diagonal.

# Problem Description

The Chessboard and Queens
In the game of chess, a queen can move any number of squares vertically, horizontally, or diagonally. Given this movement capability, the goal of the N-Queens puzzle is to place N queens on a chessboard of size N×N so that none of the queens can attack each other.

# Constraints

N must be an integer greater than or equal to 4.
No two queens can be in the same row.
No two queens can be in the same column.
No two queens can be on the same diagonal.
Solution Approach

# Backtracking Algorithm

To solve the N-Queens puzzle, we use a backtracking algorithm. Backtracking is an algorithmic technique for solving problems incrementally, one piece at a time, and removing solutions that fail to satisfy the constraints of the problem at any point in time.

Steps to Solve the Puzzle
Initialize the Board:

Represent the board as a list where the index represents the row and the value at that index represents the column where the queen is placed.
Place Queens:

Place a queen in the first row and move to the next row.
For each row, try placing a queen in each column and check if it is safe to place the queen there.
If placing the queen in the current column does not lead to a solution, backtrack and try the next column.
Check Validity:

Ensure that placing a queen does not lead to any two queens attacking each other.
Check the column and both diagonals to ensure no other queens can attack the current position.
Record Solutions:

If a valid arrangement is found where all queens are placed such that they do not attack each other, record this arrangement as a solution.
Print Solutions:

Output each solution in the specified format, with one solution per line.
Usage
The program can be executed from the command line. Here’s how to use it:

python3 nqueens.py N
Where N is the size of the chessboard (and the number of queens).

Example
To solve the 4-Queens puzzle:

python3 nqueens.py 4
This will output all possible solutions for placing 4 queens on a 4×4 chessboard.

Output Format
Each solution is printed one per line, in the following format:

[[row1, col1], [row2, col2], [row3, col3], [row4, col4], ...]
Where rowi and coli are the row and column indices (0-indexed) of the ith queen.

Error Handling
If the program is called with the wrong number of arguments, it prints:

Usage: nqueens N
If N is not an integer, it prints:

N must be a number
If N is smaller than 4, it prints:

N must be at least 4
Example Run

[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
This means that for one of the solutions, queens are placed at positions (0, 1), (1, 3), (2, 0), and (3, 2) on a 4x4 chessboard.

# Conclusion

The N-Queens puzzle is an excellent exercise in algorithm design, particularly in understanding backtracking. This solver demonstrates a practical implementation of these concepts and provides all possible solutions for any valid N.

Feel free to contribute to this project or use it to understand the intricacies of the N-Queens puzzle and backtracking algorithms.

# License

This project is licensed under the MIT License.
