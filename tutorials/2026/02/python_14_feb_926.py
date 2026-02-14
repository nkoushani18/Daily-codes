# Binary Search Algorithm in Python

def binary_search(arr, target):
    # Initialize two pointers, one at the start and one at the end of the array
    low = 0
    high = len(arr) - 1
    
    # Continue searching until the two pointers meet
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # If the target is found at the middle index, return it
        if arr[mid] == target:
            return mid
        
        # If the target is less than the middle element, move the high pointer to the left
        elif arr[mid] > target:
            high = mid - 1
            
        # If the target is greater than the middle element, move the low pointer to the right
        else:
            low = mid + 1
    
    # If the target is not found in the array, return None
    return None

# Example usage:
arr = [1, 3, 5, 7, 9]
target = 6
result = binary_search(arr, target)

if result is not None:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")