# Prefix Sum Explanation
"""
This script explains the concept of prefix sum using Python.

Prefix sum is an array where each element at index i represents the sum of all elements from the start of the array to the ith index in the original array.
"""

class PrefixSum:
    def __init__(self, nums):
        """
        Initialize the PrefixSum class with a list of numbers.
        
        :param nums: A list of numbers
        """
        self.nums = nums
        self.prefix_sum = [0] * (len(nums) + 1)

    def calculate_prefix_sum(self):
        """
        Calculate the prefix sum for the given list of numbers.
        """
        # Initialize the first element of the prefix sum array to be the same as the first number in the input list
        self.prefix_sum[0] = self.nums[0]
        
        # Iterate over the rest of the numbers and calculate their cumulative sum
        for i in range(1, len(self.nums)):
            # The ith element of the prefix sum array is the sum of the ith number and the (i-1)th element
            self.prefix_sum[i] = self.nums[i] + self.prefix_sum[i - 1]

    def get_prefix_sum_at_index(self, i):
        """
        Get the prefix sum at a given index.
        
        :param i: The index to get the prefix sum for
        :return: The prefix sum at the specified index
        """
        # If the index is out of bounds, return 0
        if i < 0 or i >= len(self.prefix_sum):
            return 0
        
        # Return the prefix sum at the specified index
        return self.prefix_sum[i]

def print_prefix_sum_array(prefix_sum_array):
    """
    Print a prefix sum array in a readable format.
    
    :param prefix_sum_array: The prefix sum array to print
    """
    for i, num in enumerate(prefix_sum_array):
        print(f"Prefix sum at index {i}: {num}")

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the prefix sum
prefix_sum = PrefixSum(numbers)
prefix_sum.calculate_prefix_sum()

# Print the prefix sum array
print_prefix_sum_array(prefix_sum.prefix_sum)

# Get the prefix sum at index 3
index_3_prefix_sum = prefix_sum.get_prefix_sum_at_index(3)
print(f"Prefix sum at index 3: {index_3_prefix_sum}")