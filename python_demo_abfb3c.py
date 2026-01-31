# --- Narrative Generator Tutorial ---
# Learning Objective: This tutorial teaches how to generate dynamic and compelling
# narratives from simple datasets in Python. We will focus on using f-strings
# for easy string formatting and conditional logic (if/elif/else statements)
# to create varied and context-aware sentences.

# --- Sample Dataset ---
# Imagine we have some data about different characters or items.
# We can represent this data as dictionaries for easy access.
# Each dictionary represents an individual entry in our dataset.

characters_data = [
    {
        "name": "Alice",
        "trait": "brave",
        "location": "forest",
        "item": "sword",
        "mood": "determined"
    },
    {
        "name": "Bob",
        "trait": "cunning",
        "location": "village",
        "item": "map",
        "mood": "curious"
    },
    {
        "name": "Charlie",
        "trait": "wise",
        "location": "mountain",
        "item": "scroll",
        "mood": "thoughtful"
    },
    {
        "name": "Diana",
        "trait": "fierce",
        "location": "ruins",
        "item": "shield",
        "mood": "angry"
    }
]

# --- Function to Generate Narrative Snippets ---

def generate_narrative_snippet(character_info):
    """
    Generates a single narrative snippet based on character information.

    This function demonstrates the use of f-strings and conditional logic
    to create varied sentences.

    Args:
        character_info (dict): A dictionary containing information about a character.
                               Expected keys: 'name', 'trait', 'location', 'item', 'mood'.

    Returns:
        str: A formatted narrative sentence.
    """

    # Extracting information from the dictionary for easier access.
    name = character_info.get("name", "Unknown") # .get() is safer than direct access, provides a default
    trait = character_info.get("trait", "peculiar")
    location = character_info.get("location", "an unspecified place")
    item = character_info.get("item", "a mysterious object")
    mood = character_info.get("mood", "neutral")

    # --- Using f-strings for dynamic text generation ---
    # f-strings (formatted string literals) are a modern and readable way
    # to embed Python expressions inside string literals. They start with 'f'
    # before the opening quote.
    # We can directly embed variable names within curly braces {}.

    # Example: A simple sentence structure.
    base_sentence = f"{name} was a {trait} adventurer, currently in the {location}."

    # --- Using conditional logic (if/elif/else) to add variety ---
    # Conditional statements allow us to change the narrative based on the
    # character's mood or other attributes. This makes the story more dynamic
    # and engaging.

    # Let's add a sentence describing what they might be doing with their item,
    # based on their mood.

    action_phrase = "" # Initialize an empty string to build upon

    if mood == "determined":
        # If the character is determined, they are likely focused on their goal.
        action_phrase = f"Clutching their {item}, they were focused on their next move."
    elif mood == "curious":
        # If curious, they might be exploring or observing.
        action_phrase = f"With their {item} in hand, they peered around, eager to discover secrets."
    elif mood == "thoughtful":
        # If thoughtful, they might be contemplating or studying.
        action_phrase = f"They studied the {item} with a deep, contemplative gaze."
    elif mood == "angry":
        # If angry, their actions might be more aggressive.
        action_phrase = f"Gripping their {item} tightly, their eyes blazed with a fierce intensity."
    else:
        # A default action if the mood isn't one of the specific cases.
        action_phrase = f"They were seen with their {item}, appearing rather preoccupied."

    # Combining the base sentence with the action phrase to form the complete snippet.
    full_snippet = f"{base_sentence} {action_phrase}"

    return full_snippet

# --- Main Function to Generate a Full Narrative ---

def generate_story(data_list):
    """
    Generates a complete narrative by iterating through a list of character data.

    Args:
        data_list (list): A list of dictionaries, where each dictionary
                          represents character information.

    Returns:
        str: The complete generated narrative.
    """
    story = "" # Initialize an empty string to build the story
    print("--- Generating Narrative ---") # Inform the user what's happening

    # Loop through each character's data in the list
    for character_info in data_list:
        # For each character, generate a narrative snippet
        snippet = generate_narrative_snippet(character_info)
        # Append the snippet to the main story string, adding a newline for readability
        story += snippet + "\n\n" # Add two newlines to separate paragraphs

    print("--- Narrative Generation Complete ---")
    return story

# --- Example Usage ---

if __name__ == "__main__":
    # This block of code will only run when the script is executed directly,
    # not when it's imported as a module. It's a standard Python practice.

    # Call the generate_story function with our sample data
    generated_narrative = generate_story(characters_data)

    # Print the resulting narrative to the console
    print(generated_narrative)

    # --- Another Example with different data ---
    # You can easily adapt this to different datasets.
    # Let's imagine a simpler scenario with just names and moods.

    items_data = [
        {"name": "Dragon's Eye Gem", "color": "red", "rarity": "legendary"},
        {"name": "Whispering Willow Leaf", "color": "green", "rarity": "common"},
        {"name": "Moonstone Pendant", "color": "blue", "rarity": "rare"}
    ]

    def describe_item(item_info):
        """Describes an item using f-strings and conditional logic."""
        name = item_info.get("name", "a curious object")
        color = item_info.get("color", "unknown color")
        rarity = item_info.get("rarity", "unknown rarity")

        description = f"The {name} shimmered with a {color} hue."

        if rarity == "legendary":
            description += " It was said to hold immense power."
        elif rarity == "rare":
            description += " Many sought after such a treasure."
        elif rarity == "common":
            description += " It was a simple, yet useful item."
        else:
            description += " Its true nature remained a mystery."

        return description

    print("\n--- Generating Item Descriptions ---")
    for item in items_data:
        print(describe_item(item))
        print("-" * 20) # Separator for clarity

    print("--- Tutorial Finished ---")

# End of Tutorial Script.
# You can now experiment with your own datasets!