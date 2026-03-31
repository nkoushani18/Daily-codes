# String Hashing in Python

# Import the necessary libraries
import hashlib

# Function to calculate the hash of a given string
def calculate_hash(string):
    # Create an instance of the SHA256 hash function
    hash_object = hashlib.sha256()
    
    # Convert the string into bytes and update the hash object
    hash_object.update(string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    
    return hex_dig

# Function to reverse a given string
def reverse_string(s):
    # Use slicing to get the characters in reverse order
    reversed_s = s[::-1]
    
    return reversed_s

# Function to calculate the length of the shortest string in a list
def shortest_length_list(string_list):
    # Initialize the minimum length with infinity
    min_len = float('inf')
    
    # Iterate over each string in the list
    for string in string_list:
        # Update the minimum length if the current string's length is smaller
        if len(string) < min_len:
            min_len = len(string)
    
    return min_len

# Test the functions with a sample string
def test_functions():
    # Define a sample string
    s = "Hello, World!"
    
    # Calculate the hash of the string
    print("Hash:", calculate_hash(s))
    
    # Reverse the string
    reversed_s = reverse_string(s)
    print("Reversed String:", reversed_s)
    
    # Define a list of strings
    string_list = ["apple", "banana", "cherry"]
    
    # Calculate the length of the shortest string in the list
    min_len = shortest_length_list(string_list)
    print("Minimum Length:", min_len)

# Run the test functions
test_functions()