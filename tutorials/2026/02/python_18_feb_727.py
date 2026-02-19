class TrieNode:
    def __init__(self):
        # Initialize a new node with an empty dictionary to store children and boolean flag to mark the end of a word
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # Initialize a new trie with a root node
        self.root = TrieNode()

    def insert(self, word):
        # Start at the root node
        current_node = self.root
        
        # Iterate over each character in the word
        for char in word:
            # If the character is not already a child of the current node, add it
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            # Move to the child node
            current_node = current_node.children[char]
        
        # Mark the end of the word
        current_node.is_end_of_word = True

    def search(self, word):
        # Start at the root node
        current_node = self.root
        
        # Iterate over each character in the word
        for char in word:
            # If the character is not a child of the current node, return False
            if char not in current_node.children:
                return False
            # Move to the child node
            current_node = current_node.children[char]
        
        # Return whether the end of the word has been marked
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        # Start at the root node
        current_node = self.root
        
        # Iterate over each character in the prefix
        for char in prefix:
            # If the character is not a child of the current node, return False
            if char not in current_node.children:
                return False
            # Move to the child node
            current_node = current_node.children[char]
        
        # Return True if we've reached this point, meaning the prefix is a prefix of all words in the trie
        return True

# Example usage
trie = Trie()

# Insert some words into the trie
words_to_insert = ["apple", "banana", "cherry"]
for word in words_to_insert:
    trie.insert(word)

# Test the search method
print(trie.search("apple"))  # Output: True
print(trie.search("grape"))   # Output: False

# Test the starts_with method
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("ban"))  # Output: True
print(trie.starts_with("cher")) # Output: True