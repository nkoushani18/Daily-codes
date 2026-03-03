class TrieNode:
    # Initialize a new TrieNode
    def __init__(self):
        self.children = {}  # Map of character to child node
        self.is_end_of_word = False  # Flag to mark the end of a word


class Trie:
    # Initialize a new Trie
    def __init__(self):
        self.root = TrieNode()  # Start with a root node


    def insert(self, word):
        # Insert a new word into the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                # If the character is not in the children, create a new node
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word


    def search(self, word):
        # Search for a word in the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                # If the character is not in the children, the word is not in the Trie
                return False
            node = node.children[char]
        return node.is_end_of_word  # Return the flag of the word


    def starts_with(self, prefix):
        # Check if there are any words in the Trie that start with the prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                # If the character is not in the children, there are no words that start with the prefix
                return False
            node = node.children[char]
        return True  # There are words that start with the prefix


# Example usage
trie = Trie()
words = ["apple", "banana", "cherry", "date", "elderberry"]
for word in words:
    trie.insert(word)

print(trie.search("apple"))  # Output: True
print(trie.search("banana"))  # Output: True
print(trie.search("cherry"))  # Output: True
print(trie.search("date"))  # Output: True
print(trie.search("elderberry"))  # Output: True
print(trie.search("grape"))  # Output: False

print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("ban"))  # Output: True
print(trie.starts_with("che"))  # Output: True
print(trie.starts_with("dat"))  # Output: True
print(trie.starts_with("eld"))  # Output: True
print(trie.starts_with("gra"))  # Output: False