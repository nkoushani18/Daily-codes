# Dynamic Programming and Memoization Example

def fibonacci(n, memo={}):
    # Base case: If n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if result for n already calculated and stored in memo dictionary
    if n not in memo:
        # Calculate the Fibonacci number using the formula n = n-1 + (n-2)
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    
    # Return the result from the memo dictionary
    return memo[n]

# Test the function with some values
print(fibonacci(10))
print(fibonacci(20))

def matrix_chain_order(p):
    # Initialize the number of matrices to n-1
    n = len(p) - 1
    
    # Create a table to store the minimum cost of multiplying matrices
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill the table using dynamic programming
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                # Calculate the cost of multiplying matrices from i to k and from k+1 to j
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    
    # Print the minimum cost of multiplying matrices
    print(m[1][n])

# Define the cost matrix for the matrix chain problem
p = [30, 35, 15, 5, 10, 20, 25]

matrix_chain_order(p)

def knapsack(W, wt, val, n):
    # Create a table to store the maximum value for each weight
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]
    
    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    
    # Return the maximum value
    return K[n][W]

# Define the weights and values of items
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print(knapsack(W, wt, val, n))