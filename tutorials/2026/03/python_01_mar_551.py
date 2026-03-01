# Divide and Conquer in Python
# This script demonstrates the concept of divide and conquer using a simple example of merging two sorted arrays.

def merge(arr1, arr2):
    # Initialize the result array
    result = []
    # Initialize pointers for both arrays
    i, j = 0, 0
    # Merge smaller elements first
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    # If there are remaining elements in either array, append them to the result
    result += arr1[i:]
    result += arr2[j:]
    return result

def merge_sort(arr):
    # If the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Merge the sorted halves
    return merge(left_half, right_half)

# Test the code
arr = [5, 2, 8, 3, 1, 4, 6]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)