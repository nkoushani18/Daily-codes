import random
def merge_sort(arr):
    # If the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []  # Initialize an empty list to store the merged result
    i = j = 0
    
    # Compare elements from both lists and add the smaller one to the merged list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # If there are any remaining elements in either the left or the right list, add them to the merged list
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Generate a random array of integers
arr = [random.randint(0,100) for _ in range(10)]
print("Original Array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)