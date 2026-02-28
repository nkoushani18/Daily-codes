# Binary Search in Python

def binary_search(arr, target):
    """
    Searches for the target element in the given array using binary search.
    
    Args:
        arr (list): The input array to be searched.
        target (int): The target element to be found.
    
    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    
    # Initialize the low and high pointers
    low = 0
    high = len(arr) - 1
    
    # Continue the search until the low pointer is less than or equal to the high pointer
    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2
        
        # If the target is found at the mid index, return the mid index
        if arr[mid] == target:
            return mid
        # If the target is less than the element at the mid index, update the high pointer
        elif arr[mid] > target:
            high = mid - 1
        # If the target is greater than the element at the mid index, update the low pointer
        else:
            low = mid + 1
    
    # If the target is not found, return -1
    return -1

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12

# Find the index of the target element
index = binary_search(arr, target)

# Print the result
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")