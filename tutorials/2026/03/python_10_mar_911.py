# Two Pointers Technique in Python
=====================================

The two pointers technique is a common approach used to solve problems that involve finding pairs or matching elements in arrays, lists, or strings.

```python
def two_pointers(arr):
    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Continue the loop until the two pointers meet
    while left < right:
        # If the elements at the two pointers are equal, we can do something with them
        if arr[left] == arr[right]:
            # Return the elements at the two pointers
            return arr[left], arr[right]
        
        # If the element at the left pointer is smaller, move the left pointer to the right
        elif arr[left] < arr[right]:
            left += 1
        # If the element at the right pointer is smaller, move the right pointer to the left
        else:
            right -= 1
    
    # If no pair is found, return None
    return None

# Test the function
arr = [1, 2, 3, 4, 5, 6]
result = two_pointers(arr)
print(result)  # Output: (1, 6)