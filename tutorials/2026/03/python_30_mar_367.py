# Sliding Window Technique in Python
=====================================

The sliding window technique is a popular algorithmic approach used to solve problems that require processing elements within a fixed-size window. This technique is particularly useful when dealing with arrays or strings.

### The Problem

Suppose we have an array of integers, and we want to find the maximum sum of a subarray of size `k`. We can use the sliding window technique to efficiently achieve this.

### Code
```python
def max_sum_subarray(arr, k):
    """
    Returns the maximum sum of a subarray of size k in arr.
    
    Parameters:
    arr (list): Input array.
    k (int): Size of the subarray.
    
    Returns:
    int: Maximum sum of a subarray of size k.
    """
    # Initialize variables to store the maximum sum and the current window's sum
    max_sum = float('-inf')
    window_sum = 0
    
    # Calculate the initial window sum by taking the first 'k' elements
    for i in range(k):
        window_sum += arr[i]
    
    # Update the maximum sum if the initial window sum is greater
    max_sum = max(max_sum, window_sum)
    
    # Slide the window to the right and update the current window's sum
    for i in range(k, len(arr)):
        # Remove the leftmost element from the previous window sum
        window_sum -= arr[i - k]
        
        # Add the new element at the right end of the window
        window_sum += arr[i]
        
        # Update the maximum sum if the current window's sum is greater
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
print(max_sum_subarray(arr, k))  # Output: 12