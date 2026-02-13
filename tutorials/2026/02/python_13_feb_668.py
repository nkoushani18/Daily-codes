# String Hashing in Python

import hashlib

def calculate_hash(string):
    """
    Calculate the hash of a given string.

    This function uses the SHA-256 hashing algorithm to generate a 32-character hash.
    The hash is calculated from the input string and returned as a hexadecimal string.
    """

    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Convert the input string to bytes and update the hash object
    hash_object.update(string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()

    return hex_dig

def string_hashing_example():
    """
    Example usage of string hashing.

    This function demonstrates how to use the calculate_hash function with two different strings.
    The hashes are compared and displayed on the console.
    """

    # Define two input strings
    str1 = "Hello, World!"
    str2 = "Python Programming"

    # Calculate the hash for each string
    hash1 = calculate_hash(str1)
    hash2 = calculate_hash(str2)

    # Display the results on the console
    print(f"Hash of {str1}: {hash1}")
    print(f"Hash of {str2}: {hash2}")

string_hashing_example()