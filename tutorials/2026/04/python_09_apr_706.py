# Merge Sort Algorithm in Python

def merge_sort(arr):
    # If the array has only one element or is empty, it's already sorted
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    print(f"Splitting: {arr} into two halves of size {len(left_half)} and {len(right_half)}")
    
    # Recursively sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    print(f"Sorting complete. Left half: {left_half}, Right half: {right_half}")
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            
    print(f"Merging: {left} and {right}. Merged result: {merged}")
    
    # Append any remaining elements from the left or right arrays
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)