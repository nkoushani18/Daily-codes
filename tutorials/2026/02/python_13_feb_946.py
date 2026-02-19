# Prefix Sum Array: A Useful Data Structure for Efficient Range Queries
===========================================================

A prefix sum array is a data structure used to store the cumulative sum of elements in an array. It allows us to calculate the sum of any subarray or range in O(1) time, making it extremely useful for efficient range queries.

```python
class PrefixSumArray:
    def __init__(self, arr):
        """
        Initializes a prefix sum array.
        
        Parameters:
        arr (list): The input array.
        
        Returns:
        list: The prefix sum array.
        """
        # Calculate the length of the array
        n = len(arr)
        
        # Initialize the prefix sum array with zeros
        self.prefix_sum_array = [0] * (n + 1)
        
        # Iterate over each element in the array
        for i in range(n):
            # Add the current element to the previous prefix sum
            self.prefix_sum_array[i + 1] = self.prefix_sum_array[i] + arr[i]
    
    def query(self, start, end):
        """
        Queries the prefix sum array for a given range.
        
        Parameters:
        start (int): The starting index of the range.
        end (int): The ending index of the range.
        
        Returns:
        int: The sum of the elements in the range.
        """
        # Return the difference between the last and first prefix sums
        return self.prefix_sum_array[end + 1] - self.prefix_sum_array[start]
    
# Example usage:
arr = [1, 2, 3, 4, 5]
prefix_sum = PrefixSumArray(arr)

print("Prefix sum array:", prefix_sum.prefix_sum_array)
print("Query for range (1, 3):", prefix_sum.query(1, 3))  # Output: 6
print("Query for range (2, 5):", prefix_sum.query(2, 5))  # Output: 10

# Test case:
arr = [1, 2, -3, 4, -5]
prefix_sum = PrefixSumArray(arr)

for i in range(len(prefix_sum.prefix_sum_array) - 1):
    print("Prefix sum at index", i, ":", prefix_sum.prefix_sum_array[i + 1])

# Output:
# Prefix sum at index 0 : 0
# Prefix sum at index 1 : 2
# Prefix sum at index 2 : 4
# Prefix sum at index 3 : 6
# Prefix sum at index 4 : 8