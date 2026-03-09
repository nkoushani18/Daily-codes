# Dynamic Programming with Memoization

## Introduction
Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem only once, and storing their solutions to subproblems to avoid redundant computation. Memoization is a technique used in dynamic programming to improve performance by caching the results of expensive function calls.

## Fibonacci Series

The Fibonacci series is a classic example of a dynamic programming problem. The problem is to find the nth Fibonacci number, where each number is the sum of the two preceding ones, usually starting with 0 and 1.

## Code

```python
def fibonacci(n, memo={}):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # If the result is already in the memo, return it
    elif n in memo:
        return memo[n]
    # Otherwise, compute the result and store it in the memo
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result

# Example usage
n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")