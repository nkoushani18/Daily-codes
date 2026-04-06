# Sliding Window Technique in Python

def max_sum_subarray(arr, k):
    """
    Find the maximum sum of a subarray of size k.
    
    Parameters:
    arr (list): Input array.
    k (int): Size of the subarray.
    
    Returns:
    int: Maximum sum of a subarray of size k.
    """
    # Calculate prefix sum to store cumulative sum at each index
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    max_sum = float('-inf')
    # Slide the window of size k over the array
    for i in range(n - k + 1):
        # Calculate sum of current subarray using prefix sum
        current_sum = prefix_sum[i + k] - prefix_sum[i]
        
        # Update maximum sum if current sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_sum(arr, k):
    """
    Find the maximum subarray of size k.
    
    Parameters:
    arr (list): Input array.
    k (int): Size of the subarray.
    
    Returns:
    list: Maximum subarray of size k.
    """
    n = len(arr)
    max_sum = float('-inf')
    max_subarray = []
    # Slide the window of size k over the array
    for i in range(n - k + 1):
        current_sum = sum(arr[i:i + k])
        
        # Update maximum sum and subarray if current sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
            max_subarray = arr[i:i + k]

    return max_subarray


# Test the functions with an example array
arr = [1, 2, 3, 4, 5]
k = 3

max_sum = max_sum_subarray(arr, k)
print("Maximum sum of subarray of size", k, "is:", max_sum)

max_subarray = max_subarray_sum(arr, k)
print("Maximum subarray of size", k, "is:", max_subarray)