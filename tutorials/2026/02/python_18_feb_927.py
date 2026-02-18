# Binary Search Algorithm Implementation in Python

def binary_search(arr, target):
    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Continue searching while the two pointers haven't crossed each other
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if the target is at the middle index
        if arr[mid] == target:
            return mid
        # If the target is less than the middle element, move the right pointer to the left
        elif arr[mid] > target:
            right = mid - 1
        # If the target is greater than the middle element, move the left pointer to the right
        else:
            left = mid + 1
    
    # If the target wasn't found, return None (or a specific value indicating an error)
    return None

# Example usage:
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search(arr, target)

if result is not None:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")