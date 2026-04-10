# Recursive Backtracking Example
```python
class Solution:
    def solve(self, board):
        # Function to mark occupied cells
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == 'O':
                return
            board[i][j] = 'T'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        # Function to mark empty cells as 'X' and the rest as 'O'
        def backtrack(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'T':
                return
            board[i][j] = 'X'
            for x in range(-1, 2):
                for y in range(-1, 2):
                    backtrack(i+x, j+y)

        # Mark occupied cells as 'O'
        for i in range(len(board)):
            dfs(0, i)
            dfs(len(board)-1, i)
        
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board[0])-1, j)

        # Mark empty cells as 'X' and the rest as 'O'
        backtrack(0, 0)

    def print_board(self, board):
        for row in board:
            print(' '.join(row))


# Test the function
if __name__ == '__main__':
    solution = Solution()
    board = [
        ['X', 'O', 'X', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['X', 'X', 'O', 'X']
    ]
    print("Original Board:")
    solution.print_board(board)
    
    solution.solve(board)
    
    print("\nSolved Board:")
    solution.print_board(board)