# String Hashing in Python

# Import the required library
import hashlib

# Function to calculate the hash of a given string
def calculate_hash(input_string):
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Convert the input string into bytes and update the hash object
    hash_object.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()

    return hex_dig

# Example usage:
if __name__ == "__main__":
    # Input string for which we want to calculate the hash
    input_str = "Hello, World!"

    # Calculate and print the hash of the input string
    calculated_hash = calculate_hash(input_str)
    print("Hash of", input_str, "is:", calculated_hash)

# Another example with a longer string:
if __name__ == "__main__":
    # Input string for which we want to calculate the hash
    input_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    # Calculate and print the hash of the input string
    calculated_hash = calculate_hash(input_str)
    print("Hash of", input_str, "is:", calculated_hash)

# Example with a random string:
if __name__ == "__main__":
    # Input string for which we want to calculate the hash
    input_str = "GUR PENML XRL VF ZL FRPERG CBFG"

    # Calculate and print the hash of the input string
    calculated_hash = calculate_hash(input_str)
    print("Hash of", input_str, "is:", calculated_hash)