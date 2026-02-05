# AI Story Generator Tutorial

# Learning Objective:
# This tutorial will teach you how to build a simple AI story generator in Python.
# We will focus on using Python's built-in 'random' module to introduce
# unpredictability and string manipulation to create branching narratives,
# allowing for a different story to be generated each time.

# Import the 'random' module.
# The 'random' module is essential for generating random choices.
# We'll use it to pick random elements from lists, which will form
# the building blocks of our story.
import random

# --- Story Components ---
# We'll define lists of potential story elements.
# Each list represents a category of words or phrases that can be
# inserted into our story at specific points.

# List of possible protagonists.
# These are the main characters of our stories.
protagonists = [
    "a brave knight",
    "a curious wizard",
    "a clever rogue",
    "a lonely robot",
    "a talking cat"
]

# List of possible settings.
# These are the places where our stories will take place.
settings = [
    "in a mystical forest",
    "in a bustling medieval city",
    "on a distant alien planet",
    "in a forgotten ancient ruin",
    "in a cozy hobbit hole"
]

# List of possible objectives or quests.
# These are the goals our protagonists will try to achieve.
objectives = [
    "to find a lost treasure",
    "to rescue a captured princess",
    "to defeat a fearsome dragon",
    "to uncover a hidden secret",
    "to deliver a magical artifact"
]

# List of possible challenges or obstacles.
# These are the difficulties the protagonists might face.
challenges = [
    "they encountered a mischievous goblin",
    "they had to solve a cunning riddle",
    "they were chased by a ferocious beast",
    "they got lost in a magical maze",
    "they had to outsmart a cunning sorcerer"
]

# List of possible outcomes or resolutions.
# These are how the stories might end.
outcomes = [
    "and lived happily ever after.",
    "but learned a valuable lesson.",
    "and became a legend.",
    "only to find a new adventure waiting.",
    "and found unexpected friendship."
]

# --- Story Generation Function ---

def generate_story():
    # This function will assemble a complete story by randomly selecting
    # elements from our predefined lists.

    # Randomly choose a protagonist from the 'protagonists' list.
    # The random.choice() function picks one item at random from a sequence (like a list).
    chosen_protagonist = random.choice(protagonists)

    # Randomly choose a setting from the 'settings' list.
    chosen_setting = random.choice(settings)

    # Randomly choose an objective from the 'objectives' list.
    chosen_objective = random.choice(objectives)

    # Randomly choose a challenge from the 'challenges' list.
    chosen_challenge = random.choice(challenges)

    # Randomly choose an outcome from the 'outcomes' list.
    chosen_outcome = random.choice(outcomes)

    # Now, we'll construct the story string.
    # We use f-strings (formatted string literals) for easy embedding of variables.
    # This is a modern and readable way to create strings with dynamic content.
    story = f"Once upon a time, {chosen_protagonist} lived {chosen_setting}. "
    story += f"Their quest was {chosen_objective}. "
    story += f"In their journey, {chosen_challenge}. "
    story += f"After overcoming the obstacle, {chosen_protagonist} {chosen_outcome}"

    # Return the complete, randomly generated story.
    return story

# --- Example Usage ---

# This is where we call our function and print the result.
# This demonstrates how to use the 'generate_story' function.

if __name__ == "__main__":
    # The 'if __name__ == "__main__":' block ensures that this code
    # only runs when the script is executed directly (not when imported
    # as a module into another script). This is good practice.

    print("Welcome to the Simple AI Story Generator!")
    print("-" * 30) # Print a separator line for better readability.

    # Generate and print the first story.
    story1 = generate_story()
    print("Story 1:")
    print(story1)
    print("\n") # Add an extra newline for spacing between stories.

    # Generate and print a second story to show the randomness.
    story2 = generate_story()
    print("Story 2:")
    print(story2)
    print("\n")

    # Generate and print a third story.
    story3 = generate_story()
    print("Story 3:")
    print(story3)
    print("-" * 30)

# End of tutorial. You can now experiment by adding more elements to the lists
# or by creating new categories of story components!