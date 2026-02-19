# Sliding Window Technique: A Python Implementation

# This script teaches the sliding window technique, a fundamental algorithmic concept used in string manipulation and optimization problems.
# The technique is useful for solving problems that involve finding patterns or maximizing/minimizing values within a fixed-size window.

def max_sum_subarray(arr, k):
    """
    Returns the maximum sum of a subarray with size 'k'.
    
    Parameters:
    arr (list): The input array.
    k (int): The size of the sliding window.
    
    Returns:
    int: The maximum sum of a subarray with size 'k'.
    """
    # Initialize the maximum sum and the current sum to negative infinity
    max_sum = float('-inf')
    curr_sum = 0
    
    # Initialize two pointers for the sliding window
    left = 0
    right = 0
    
    # Iterate over the array
    while right < len(arr):
        # Add the element at the right pointer to the current sum
        curr_sum += arr[right]
        
        # If the window size exceeds 'k', subtract the element at the left pointer from the current sum and move the left pointer to the right
        if right - left + 1 > k:
            curr_sum -= arr[left]
            left += 1
        
        # Update the maximum sum if the current sum is greater
        if right - left + 1 == k and curr_sum > max_sum:
            max_sum = curr_sum
        
        # Move the right pointer to the next element
        right += 1
    
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3

max_sum = max_sum_subarray(arr, k)
print(f"Maximum sum of subarray with size {k}: {max_sum}")

# Test case 1: All positive numbers
arr = [1, 2, 3, 4, 5]
k = 3
expected_max_sum = 12
assert max_sum_subarray(arr, k) == expected_max_sum

# Test case 2: Negative numbers
arr = [-1, -2, -3, -4, -5]
k = 3
expected_max_sum = 0
assert max_sum_subarray(arr, k) == expected_max_sum

# Test case 3: Mixed numbers
arr = [1, -2, 3, -4, 5]
k = 3
expected_max_sum = 9
assert max_sum_subarray(arr, k) == expected_max_sum