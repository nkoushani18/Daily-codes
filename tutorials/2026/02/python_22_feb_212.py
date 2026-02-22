# Recursive Backtracking

# The goal of recursive backtracking is to explore all possible solutions to a problem
# by making recursive calls and then backtracking when a dead end is reached.

def solve_sudoku(board):
    # Find the first empty space
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Make a recursive call to try a number from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        # Backtrack if the current number doesn't lead to a solution
                        board[i][j] = 0
                return False
    # If all numbers have been tried and no solution is found, return False
    return True

def is_valid(board, row, col, num):
    # Check if the number already exists in the row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    # Check if the number already exists in the 3x3 sub-grid
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# Test the function
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    for row in board:
        print(row)
else:
    print("No solution exists")