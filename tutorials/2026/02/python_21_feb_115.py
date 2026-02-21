# Binary Search in Python
# This program demonstrates the binary search algorithm, which is used to find an element in a sorted list.

def binary_search(arr, target):
    # Initialize the low and high pointers
    low = 0
    high = len(arr) - 1

    # Continue the search until the low pointer is less than or equal to the high pointer
    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2

        # If the target is equal to the middle element, return the mid index
        if arr[mid] == target:
            return mid
        # If the target is less than the middle element, update the high pointer
        elif arr[mid] > target:
            high = mid - 1
        # If the target is greater than the middle element, update the low pointer
        else:
            low = mid + 1

    # If the target is not found, return -1
    return -1

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9
result = binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found in the array")