# Trie Data Structure Implementation in Python

class Node:
    # Initialize a node with a default value and an empty dictionary for children
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end_of_word = False


class Trie:
    # Initialize the trie data structure with a root node
    def __init__(self):
        self.root = Node("")


    # Insert a word into the trie
    def insert(self, word):
        # Start at the root node
        current_node = self.root
        for char in word:
            # If the character is not already in the children of the current node,
            # add it and move to its child
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        # Mark the last node as the end of a word
        current_node.is_end_of_word = True


    # Search for a word in the trie
    def search(self, word):
        # Start at the root node
        current_node = self.root
        for char in word:
            # If the character is not in the children of the current node,
            # return False because the word is not found
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # Return True if the last node marks the end of a word
        return current_node.is_end_of_word


    # Check for prefix matching in the trie
    def starts_with(self, prefix):
        # Start at the root node
        current_node = self.root
        for char in prefix:
            # If the character is not in the children of the current node,
            # return False because there's no match
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # Return True if we've reached this point, indicating a valid prefix
        return True


# Example usage
trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("apples"))  # Output: False

print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("ban"))   # Output: False