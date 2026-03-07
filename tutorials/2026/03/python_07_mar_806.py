def compute_prefix_function(pattern):
    # Initialize prefix table with zeros
    prefix = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        # If the current character matches the character at the current prefix position
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        # If the current character matches the character at the current prefix position
        if pattern[i] == pattern[j]:
            j += 1
        # Update the prefix table
        prefix[i] = j
    return prefix

def knuth_morris_pratt(text, pattern):
    # Compute prefix table for the pattern
    prefix = compute_prefix_function(pattern)
    # Initialize the search position
    j = 0
    # Iterate over the text
    for i in range(len(text)):
        # If the current character in the text matches the character at the current prefix position
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        # If the current character in the text matches the character at the current prefix position
        if text[i] == pattern[j]:
            j += 1
        # If the current prefix position is at the end of the pattern, we have a match
        if j == len(pattern):
            print(f"Found pattern '{pattern}' at position {i - j + 1}")
            j = prefix[j - 1]

# Test the algorithm
text = "banana"
pattern = "ana"
knuth_morris_pratt(text, pattern)