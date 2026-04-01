# Sliding Window Technique in Python
=====================================

This script demonstrates the use of the sliding window technique to solve a common problem in algorithms.

```python
def max_sum_subarray(arr, k):
    """
    This function calculates the maximum sum of a subarray with size k.
    
    Parameters:
    arr (list): The input array.
    k (int): The size of the subarray.
    
    Returns:
    int: The maximum sum of a subarray with size k.
    """

    # Initialize the window boundaries
    left = 0
    
    # Initialize the current sum and maximum sum
    curr_sum = 0
    max_sum = float('-inf')
    
    # Iterate over the array
    for right in range(len(arr)):
        # Add the current element to the current sum
        curr_sum += arr[right]
        
        # If the window size is greater than k, remove the leftmost element
        if right - left + 1 > k:
            curr_sum -= arr[left]
            left += 1
        
        # Update the maximum sum
        if right - left + 1 == k and curr_sum > max_sum:
            max_sum = curr_sum
    
    return max_sum

# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
print(max_sum_subarray(arr, k))  # Output: 12