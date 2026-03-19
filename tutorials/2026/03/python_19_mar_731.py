def solve_sudoku(board):
    # Find an empty space on the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try numbers from 1 to 9
                for num in range(1, 10):
                    # Check if the number is valid in this position
                    if is_valid(board, i, j, num):
                        # Place the number on the board
                        board[i][j] = num

                        # Recursively try numbers for other empty spaces
                        if solve_sudoku(board):
                            return True

                        # If we couldn't find a valid number for this space,
                        # remove it and try another number
                        board[i][j] = 0

                # If we've tried all numbers and none of them worked,
                # return False to backtrack
                return False

    # If we've filled in the entire board, return True
    return True


def is_valid(board, row, col, num):
    # Check if the number already exists in this row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number exists in the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    # If the number is valid, return True
    return True


# Create a sample Sudoku board
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

# Solve the Sudoku board
if solve_sudoku(board):
    # Print the solved board
    for row in board:
        print(row)
else:
    print("No solution exists")