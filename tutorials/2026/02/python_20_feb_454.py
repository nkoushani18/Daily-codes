# Dynamic Programming with Memoization

def fibonacci(n, memo={}):
    # Base case
    if n <= 0:
        return 0
    # Check if the result is already computed
    elif n in memo:
        return memo[n]
    # Compute the result
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        # Store the result
        memo[n] = result
        return result

# Example usage
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# Optimized version using memoization
def fibonacci_optimized(n):
    memo = [0] * (n+1)
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

# Example usage
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_optimized(i)}")