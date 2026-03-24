# Dynamic Programming with Memoization
================

This example shows how to use memoization in Python for a classic dynamic programming problem.

```python
def fibonacci(n, memo = {}):
    # Base cases: if n is 0 or 1, return the value directly
    if n <= 1:
        return n
    
    # Check if the result is already in the memo dictionary
    if n not in memo:
        # If it's not, calculate the result and store it in the memo
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    
    # Return the calculated value from the memo
    return memo[n]

# Test the function with some values
for i in range(10):
    print(fibonacci(i))