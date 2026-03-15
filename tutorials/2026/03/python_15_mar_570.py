# String Hashing in Python

# Import the required modules
import hashlib

# Define a function to calculate the hash of a string
def calculate_hash(input_string):
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Convert the input string into bytes and update the hash object with it
    hash_object.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()

    return hash_hex

# Define a function to perform string hashing for collision detection
def string_hashing_collision_detection(input_string):
    # Create a dictionary to store the hashes as keys and their corresponding strings as values
    hash_dict = {}

    # Initialize a counter to generate new hash values in case of collisions
    counter = 0

    while True:
        # Calculate the hash for the current input string
        hash_hex = calculate_hash(input_string + str(counter))

        # Check if the generated hash already exists in the dictionary
        if hash_hex not in hash_dict:
            # If it doesn't exist, add the string and its hash to the dictionary
            hash_dict[hash_hex] = input_string + str(counter)
            break
        else:
            counter += 1

    return counter

# Test the functions with an example
if __name__ == "__main__":
    input_str = "Hello, World!"
    print("Input String: ", input_str)

    # Calculate and display the hash of the input string
    hash_hex = calculate_hash(input_str)
    print("Hash (SHA-256): ", hash_hex)

    # Perform collision detection using string hashing
    counter_value = string_hashing_collision_detection(input_str)

    print("Counter Value for Collision Detection: ", counter_value)