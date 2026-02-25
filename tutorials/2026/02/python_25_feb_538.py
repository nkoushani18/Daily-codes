# Trie Data Structure Implementation in Python

class TrieNode:
    """A node in the trie data structure."""
    def __init__(self):
        # Initialize an empty dictionary to store children nodes
        self.children = {}
        # Initialize a flag to mark the end of a word
        self.is_end_of_word = False


class Trie:
    """A trie data structure implementation."""
    def __init__(self):
        # Initialize the root node
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        # Start at the root node
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word):
        """Search for a word in the trie."""
        # Start at the root node
        node = self.root
        # Iterate over each character in the word
        for char in word:
            # If the character is not in the node's children, return False
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Return True if the word is in the trie and False otherwise
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Check if any word in the trie starts with the given prefix."""
        # Start at the root node
        node = self.root
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not in the node's children, return False
            if char not in node.children:
                return False
            # Move to the child node
            node = node.children[char]
        # Return True if the prefix is in the trie and False otherwise
        return True


# Create a trie
trie = Trie()

# Insert words into the trie
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

# Search for words in the trie
print(trie.search("apple"))  # Output: True
print(trie.search("app"))  # Output: True
print(trie.search("banana"))  # Output: True
print(trie.search("ban"))  # Output: False

# Check prefixes in the trie
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("ban"))  # Output: True
print(trie.starts_with("ora"))  # Output: False