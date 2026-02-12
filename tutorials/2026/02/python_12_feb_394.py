# Binary Search Algorithm in Python

def binary_search(arr, target):
    """
    Searches for an element in a sorted array using the binary search algorithm.
    
    Parameters:
    arr (list): The sorted list to search in.
    target: The value to search for.
    
    Returns:
    int: The index of the target value if found, -1 otherwise.
    """

    # Initialize two pointers, one at the start and one at the end of the array
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Compare the middle element with the target value
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # If the middle element is less than the target, move the low pointer to mid + 1
            low = mid + 1
        else:
            # If the middle element is greater than the target, move the high pointer to mid - 1
            high = mid - 1

    # If the loop ends without finding the target, return -1
    return -1


# Example usage:

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23
index = binary_search(arr, target_value)

if index != -1:
    print(f"Target value {target_value} found at index {index}.")
else:
    print(f"Target value {target_value} not found in the array.")