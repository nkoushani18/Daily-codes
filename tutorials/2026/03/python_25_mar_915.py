# Prefix Sum with Python
=====================================

## Introduction
------------

Prefix sum is an efficient algorithm for calculating the sum of elements in a given range within a sorted array. This implementation uses Python to demonstrate how to calculate prefix sums using two methods: manual calculation and dynamic programming.

## Manual Calculation Method
-------------------------

This method involves iterating through the array and manually calculating the sum at each index by adding the current element to the previous prefix sum.

```python
def manual_prefix_sum(arr):
    # Initialize an empty list to store the prefix sums
    prefix_sums = [0] * len(arr)
    
    # Iterate over the array and calculate the prefix sums
    for i in range(len(arr)):
        if i == 0:
            prefix_sums[i] = arr[i]
        else:
            prefix_sums[i] = prefix_sums[i-1] + arr[i]
            
    return prefix_sums

# Example usage
arr = [1, 2, 3, 4, 5]
print(manual_prefix_sum(arr))
```

## Dynamic Programming Method
---------------------------

This method uses dynamic programming to store the prefix sums in an array and reuse them whenever necessary.

```python
def dynamic_prefix_sum(arr):
    # Initialize a list to store the prefix sums with the first element being the original array
    prefix_sums = [arr[0]]
    
    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        # Calculate the prefix sum by adding the current element to the previous prefix sum
        next_prefix_sum = prefix_sums[i-1] + arr[i]
        prefix_sums.append(next_prefix_sum)
        
    return prefix_sums

# Example usage
arr = [1, 2, 3, 4, 5]
print(dynamic_prefix_sum(arr))
```

## Binary Indexed Tree (BIT) Method
---------------------------------

This method uses a binary indexed tree to store the prefix sums and supports efficient range queries.

```python
class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
        
    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
            
    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
            
        return sum

def bit_prefix_sum(arr):
    # Initialize a BIT object with the length of the array
    bit = BIT(len(arr))
    
    # Iterate over the array and update the BIT for each element
    for i, num in enumerate(arr):
        bit.update(i + 1, num)
        
    return bit

# Example usage
arr = [1, 2, 3, 4, 5]
bit = bit_prefix_sum(arr)

def query_range(bit, start, end):
    # Calculate the sum of elements in the range using the BIT
    return bit.query(end) - bit.query(start - 1)
    
print(query_range(bit, 1, 4))
```

## Example Usage
-----------------