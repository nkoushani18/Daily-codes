# Two Pointers Tutorial

# Importing necessary modules
# No need to import any module for this problem

# Function to find the first duplicate in an array
def find_first_duplicate(arr):
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = 1
    
    # Continue the process until the right pointer is less than the length of the array
    while right < len(arr):
        # If the elements at the left and right pointers are the same
        if arr[left] == arr[right]:
            # Move the right pointer to the next element
            # But we still need to check if the element is a duplicate
            right += 1
            # If the element at the right pointer is the same as the element at the left pointer
            if arr[right] == arr[left]:
                # Return the index of the left pointer
                return left
        else:
            # Move the left pointer to the next element
            left += 1
        # Move the right pointer to the next element
        right += 1
    # If no duplicate is found, return -1
    return -1

# Function to find the last duplicate in an array
def find_last_duplicate(arr):
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Continue the process until the right pointer is greater than or equal to the left pointer
    while left < right:
        # If the elements at the left and right pointers are the same
        if arr[left] == arr[right]:
            # Move the right pointer to the previous element
            # But we still need to check if the element is a duplicate
            right -= 1
            # If the element at the left pointer is the same as the element at the right pointer
            if arr[left] == arr[right]:
                # Return the index of the left pointer
                return left
        else:
            # Move the left pointer to the next element
            left += 1
        # Move the right pointer to the previous element
        right -= 1
    # If no duplicate is found, return -1
    return -1

# Function to find the first pair of elements in an array that add up to a given sum
def find_sum(arr, target):
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Continue the process until the right pointer is less than the left pointer
    while left < right:
        # If the sum of the elements at the left and right pointers is equal to the target
        if arr[left] + arr[right] == target:
            # Return the indices of the left and right pointers
            return (left, right)
        # If the sum of the elements at the left and right pointers is less than the target
        elif arr[left] + arr[right] < target:
            # Move the left pointer to the next element
            left += 1
        # If the sum of the elements at the left and right pointers is greater than the target
        else:
            # Move the right pointer to the previous element
            right -=