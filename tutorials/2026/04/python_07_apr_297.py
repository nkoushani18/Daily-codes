import copy

def solve_sudoku(board):
    # Find the first empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try numbers from 1 to 9
                for num in range(1, 10):
                    # Check if number is valid
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        # If it doesn't work out, reset the cell to empty
                        board[i][j] = 0
                return False
    return True

def is_valid(board, row, col, num):
    # Check if number already exists in row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    # Check if number exists in 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# Example usage:
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