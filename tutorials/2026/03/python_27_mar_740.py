# Sliding Window Algorithm in Python
=====================================================

The sliding window algorithm is used to find elements within an array that satisfy a certain condition. This technique can be very efficient when dealing with large arrays and the problem requires checking every possible element.

## Problem Statement

We have an array of integers, and we want to find all unique elements in the array using a sliding window approach.

## Code
```python
def find_unique_elements(arr):
    # Initialize an empty set to store unique elements
    unique_elements = set()
    
    # Iterate over the array with a sliding window of size 1
    for i in range(len(arr)):
        # Add current element to the set
        unique_elements.add(arr[i])
        
    # Return the number of unique elements found
    return len(unique_elements)

# Run the function with an example array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
unique_count = find_unique_elements(arr)
print("Number of unique elements:", unique_count)