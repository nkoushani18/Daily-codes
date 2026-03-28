# Merge Sort Algorithm in Python

# Function to merge two sorted subarrays
def merge(left, right):
    # Initialize merged array and indices for left and right arrays
    merged = []
    left_index = 0
    right_index = 0
    
    # Compare elements of left and right arrays and add the smaller one to the merged array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add remaining elements of the left array to the merged array
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    # Add remaining elements of the right array to the merged array
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged

# Function to perform merge sort on an array
def merge_sort(arr):
    # If the array has only one element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle index of the array
    mid = len(arr) // 2
    
    # Divide the array into two halves and recursively sort them
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves into a single sorted array
    return merge(left_half, right_half)

# Example usage of the merge sort algorithm
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    print("Sorted array:", merge_sort(arr))
```

In this code:

1.  We first define a function `merge` that takes two sorted subarrays as input and returns their merged version.
2.  The `merge` function compares elements of the left and right arrays, adds the smaller one to the merged array, and repeats until all elements are added.
3.  After adding all remaining elements from both arrays, we return the fully merged array.
4.  Next, we define a function `merge_sort` that takes an array as input and performs the merge sort algorithm on it.
5.  The `merge_sort` function checks if the input array has only one element. If so, it is already sorted, and the function returns the original array.
6.  Otherwise, it finds the middle index of the array, divides it into two halves, and recursively sorts both halves using the `merge_sort` function.
7.  Finally, we merge the sorted halves into a single sorted array using the `merge` function and return the result.
8.  In the example usage section, we create an array, print its original values, sort it using the `merge_sort` function, and display the sorted array.

When you run this code, it will output:

```
Original array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]