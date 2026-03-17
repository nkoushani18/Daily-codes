# Dynamic Programming with Memoization Example

def fibonacci(n, memo={}):
    """
    Calculate the nth Fibonacci number using dynamic programming with memoization.
    
    Args:
        n (int): The position of the Fibonacci number to calculate.
        memo (dict): A dictionary to store previously calculated values. Defaults to {}.
    
    Returns:
        int: The nth Fibonacci number.
    """

    # Base case: If n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Check if the value has already been calculated
    if n not in memo:
        # Calculate the value recursively and store it in the dictionary
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    # Return the stored or calculated value
    return memo[n]


# Example usage:
if __name__ == "__main__":
    n = 10
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")