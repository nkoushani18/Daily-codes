# Prefix Sum Example in Python
=====================================

## Introduction
Prefix sum is an efficient method to solve many problems on arrays and lists by calculating the cumulative sum from left to right.

## Code
```python
class PrefixSum:
    def __init__(self, arr):
        """
        Initialize the prefix sum array with the input array.
        
        Args:
            arr (list): The input array.
        """
        self.n = len(arr)
        # Create a new array where each element is the cumulative sum from left to right
        self.prefix_sum = [0] * (self.n + 1)
        for i in range(self.n):
            self.prefix_sum[i + 1] = arr[i] + self.prefix_sum[i]

    def get_prefix_sum(self, low, high):
        """
        Get the prefix sum from index `low` to `high`.
        
        Args:
            low (int): The starting index.
            high (int): The ending index.
        
        Returns:
            int: The prefix sum from index `low` to `high`.
        """
        return self.prefix_sum[high + 1] - self.prefix_sum[low]

    def get_range_sum(self, low, high):
        """
        Get the range sum of all elements from index `low` to `high`.
        
        Args:
            low (int): The starting index.
            high (int): The ending index.
        
        Returns:
            int: The range sum of all elements from index `low` to `high`.
        """
        return self.get_prefix_sum(low, high) - self.prefix_sum[low]

    def get_total_sum(self):
        """
        Get the total sum of all elements in the array.
        
        Returns:
            int: The total sum of all elements in the array.
        """
        return self.prefix_sum[self.n]


# Example usage
arr = [1, 2, 3, 4, 5]
prefix_sum_obj = PrefixSum(arr)

print("Prefix sum:", prefix_sum_obj.prefix_sum)
print("Get prefix sum from index 1 to 3:", prefix_sum_obj.get_prefix_sum(1, 3))
print("Get range sum of elements from index 0 to 2:", prefix_sum_obj.get_range_sum(0, 2))
print("Get total sum:", prefix_sum_obj.get_total_sum())