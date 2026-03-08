# Prefix Sum Data Structure

# Definition of a list to store prefix sum
class PrefixSum:
    def __init__(self, arr):
        # Initialize an empty list to store prefix sum
        self.prefix_sum = [0] * (len(arr) + 1)
        
        # Calculate prefix sum and store it in the list
        for i in range(len(arr)):
            # The prefix sum at index i is the sum of all elements in the array up to index i
            self.prefix_sum[i+1] = self.prefix_sum[i] + arr[i]

    # Function to get the prefix sum at a given index
    def get_prefix_sum(self, i):
        # If i is 0, return 0 because the prefix sum at index 0 is 0
        if i == 0:
            return 0
        # Return the prefix sum at index i
        return self.prefix_sum[i+1] - self.prefix_sum[i]

    # Function to get the range of prefix sum from index a to index b
    def get_range(self, a, b):
        # If a is greater than b, return 0
        if a > b:
            return 0
        # Return the difference between the prefix sum at index b and the prefix sum at index a
        return self.prefix_sum[b+1] - self.prefix_sum[a]

# Test the prefix sum data structure
def test_prefix_sum(arr):
    # Create an instance of PrefixSum with the input array
    prefix_sum = PrefixSum(arr)
    
    # Get the prefix sum at index 3
    prefix_sum_at_index_3 = prefix_sum.get_prefix_sum(3)
    # Get the prefix sum at index 7
    prefix_sum_at_index_7 = prefix_sum.get_prefix_sum(7)
    
    # Get the range of prefix sum from index 3 to index 7
    range_of_prefix_sum = prefix_sum.get_range(3, 7)
    
    # Print the results
    print("Prefix sum at index 3:", prefix_sum_at_index_3)
    print("Prefix sum at index 7:", prefix_sum_at_index_7)
    print("Range of prefix sum from index 3 to index 7:", range_of_prefix_sum)

# Test the prefix sum data structure with an example array
test_prefix_sum([1, 2, 3, 4, 5])