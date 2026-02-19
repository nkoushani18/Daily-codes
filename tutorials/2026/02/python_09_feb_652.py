# Binary Search Algorithm in Python
#=====================================

# This script teaches the binary search algorithm, a popular searching technique used for ordered arrays.
# It's useful when you need to find an element in a sorted array efficiently.

def binary_search(arr, target):
    # Initialize two pointers at the start and end of the array
    left = 0
    right = len(arr) - 1

    # Continue the search until the two pointers meet
    while left <= right:
        # Calculate the middle index of the current range
        mid = (left + right) // 2

        # Compare the target element with the middle element
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # If the target is greater, move the left pointer to mid + 1
            left = mid + 1
        else:
            # If the target is smaller, move the right pointer to mid - 1
            right = mid - 1

    # If the target element is not found, return None
    return None


# Example usage / test
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 12
index = binary_search(arr, target)

if index is not None:
    print(f"Target element {target} found at index {index}.")
else:
    print(f"Target element {target} not found in the array.")

# Test with a different array and target element
arr = [1, 3, 5, 7, 9]
target = 6
index = binary_search(arr, target)

if index is not None:
    print(f"Target element {target} found at index {index}.")
else:
    print(f"Target element {target} not found in the array.")