# HashMap Class Implementation in Python

class HashMap:
    def __init__(self):
        # Initialize the size of the HashMap
        self.size = 10
        # Create a list to store the buckets
        self.buckets = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Calculate the index using the formula: index = (key * 31) % size
        return (hash(key) * 31) % self.size

    def insert(self, key, value):
        # Find the bucket where the key will be stored
        index = self.hash_function(key)
        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                # If it exists, update its value
                self.buckets[index][i] = (key, value)
                return
        # If not, add a new entry to the bucket
        self.buckets[index].append((key, value))

    def get(self, key):
        # Find the bucket where the key will be stored
        index = self.hash_function(key)
        # Check if the key exists in the bucket
        for k, v in self.buckets[index]:
            if k == key:
                return v
        # If not found, return None
        return None

    def remove(self, key):
        # Find the bucket where the key will be stored
        index = self.hash_function(key)
        # Check if the key exists in the bucket
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                return

    def display(self):
        # Display all entries in the HashMap
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}:")
            for key, value in bucket:
                print(f"{key}: {value}")


# Example usage
if __name__ == "__main__":
    # Create a new HashMap instance
    my_map = HashMap()
    
    # Insert entries into the HashMap
    my_map.insert("John", 25)
    my_map.insert("Alice", 30)
    my_map.insert("Bob", 35)

    # Display all entries in the HashMap
    print("HashMap Contents:")
    my_map.display()

    # Retrieve a value from the HashMap
    print(f"John's age: {my_map.get('John')}")

    # Remove an entry from the HashMap
    my_map.remove("Alice")
    
    # Display updated contents of the HashMap
    print("\nUpdated HashMap Contents:")
    my_map.display()