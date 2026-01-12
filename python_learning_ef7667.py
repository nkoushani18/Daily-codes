# Learning Objective:
# This tutorial teaches how to generate unique ASCII art poems by
# combining user input with simple artistic algorithms in Python.
# We will focus on the concept of procedural generation, where
# art is created through a set of rules and randomness, rather than
# by hand.

import random # Import the random module for generating random numbers and choices.

def get_user_input():
    """
    Prompts the user for keywords to be incorporated into the poem.
    This function handles getting creative input from the user.
    """
    print("Welcome to the ASCII Art Poem Generator!")
    print("Please enter a few keywords that inspire you. These will be woven into your poem.")
    keywords_str = input("Enter your keywords, separated by commas (e.g., 'stars, dreams, night'): ")
    # Split the input string by commas and remove any leading/trailing whitespace from each keyword.
    keywords = [keyword.strip() for keyword in keywords_str.split(',')]
    return keywords

def select_artistic_style():
    """
    Allows the user to choose from predefined artistic styles for their ASCII art.
    This introduces the idea of 'styles' or 'themes' in generation.
    """
    print("\nChoose an artistic style for your poem:")
    styles = {
        "1": "Geometric",   # A style that might use repeating patterns and straight lines.
        "2": "Organic",     # A style that might use more fluid shapes and curves.
        "3": "Abstract"     # A style that might be more freeform and less structured.
    }
    for key, value in styles.items():
        print(f"{key}: {value}")

    while True: # Loop until valid input is received.
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in styles:
            return styles[choice] # Return the selected style name.
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def generate_line_element(style, keyword):
    """
    Generates a single ASCII art line element, influenced by the chosen style and a keyword.
    This is the core of our 'artistic algorithm'.
    """
    # Define basic ASCII characters for different styles.
    geometric_chars = ['-', '=', '+', '|', '/', '\\']
    organic_chars = ['~', '*', '.', 'o', 'O', '#']
    abstract_chars = ['^', '&', '$', '%', '@', '!']

    # Select the character set based on the chosen style.
    if style == "Geometric":
        char_set = geometric_chars
    elif style == "Organic":
        char_set = organic_chars
    else: # Abstract
        char_set = abstract_chars

    # Use randomness to create variation.
    # The likelihood of using a keyword character is higher.
    char_to_use = random.choice(char_set)
    if random.random() < 0.4: # 40% chance to incorporate a keyword character.
        char_to_use = random.choice(keyword) # Use a character from the user's keyword.

    # Add some variation in length and formatting.
    length = random.randint(5, 20) # Line length between 5 and 20 characters.
    padding_amount = random.randint(0, 5) # Random padding for visual spacing.

    # Create the line with padding.
    padding = " " * padding_amount
    line = padding + "".join(random.choice(char_to_use) for _ in range(length)) + padding
    return line

def generate_ascii_poem(keywords, style, num_lines=5):
    """
    Generates the complete ASCII art poem.
    This function orchestrates the poem's structure.
    """
    poem_lines = []
    for _ in range(num_lines): # Generate a specified number of lines for the poem.
        # Pick a random keyword for this line to ensure variety.
        current_keyword = random.choice(keywords) if keywords else ""
        poem_lines.append(generate_line_element(style, current_keyword))
    return "\n".join(poem_lines) # Join all generated lines with newline characters.

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Get creative input from the user.
    user_keywords = get_user_input()

    # 2. Let the user choose the artistic feel.
    selected_style = select_artistic_style()

    # 3. Generate the poem using the user's input and the chosen style.
    print("\n--- Your Unique ASCII Art Poem ---")
    poem = generate_ascii_poem(user_keywords, selected_style, num_lines=7) # Generate a 7-line poem.
    print(poem)
    print("----------------------------------")

    # This example demonstrates how to combine user input with simple rules
    # (character sets, length variation, keyword inclusion) to create
    # procedurally generated art. Experiment with different keywords and styles!