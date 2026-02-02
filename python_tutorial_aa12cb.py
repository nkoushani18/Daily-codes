# Learning Objective:
# This tutorial will guide you through building a simple text-based adventure game in Python.
# The core focus is on understanding how to process player input using basic Natural Language Processing (NLP) techniques.
# We will learn to extract keywords from player commands to determine their intended action.
# This approach makes the game more interactive and less rigid than requiring exact command matching.

import random # Import the random module for potential future use (e.g., random events)

# --- Game State and Data ---

# Represents the player's current location and inventory.
player_state = {
    "location": "forest_entrance",
    "inventory": []
}

# Defines the rooms in our game world.
# Each room has a description and a list of possible exits.
# The keys are the room IDs.
rooms = {
    "forest_entrance": {
        "description": "You stand at the edge of a dark, mysterious forest. A narrow path leads deeper in.",
        "exits": {"north": "forest_path"}
    },
    "forest_path": {
        "description": "The path winds through tall, ancient trees. Sunlight struggles to break through the canopy.",
        "exits": {"south": "forest_entrance", "east": "clearing"}
    },
    "clearing": {
        "description": "You've reached a small, sun-dappled clearing. In the center, a shimmering object rests on a pedestal.",
        "exits": {"west": "forest_path"}
    }
}

# --- NLP Functions (Keyword Extraction) ---

def get_keywords(command):
    # This function takes a player's command string and extracts relevant keywords.
    # For simplicity, we'll consider common verbs and nouns.
    # In a more complex game, you'd use more sophisticated NLP libraries.

    command = command.lower() # Convert the command to lowercase for case-insensitive matching.
    words = command.split() # Split the command into individual words.

    # Define lists of common action verbs and nouns relevant to our game.
    action_verbs = ["go", "move", "walk", "take", "get", "pick", "look", "examine"]
    nouns = ["north", "south", "east", "west", "object", "item", "path", "forest", "clearing", "pedestal"]

    extracted_keywords = []
    for word in words:
        if word in action_verbs:
            extracted_keywords.append(("verb", word)) # Tag as a verb
        elif word in nouns:
            extracted_keywords.append(("noun", word)) # Tag as a noun

    return extracted_keywords

# --- Game Logic Functions ---

def display_location():
    # Prints the description of the player's current location.
    current_room_id = player_state["location"]
    room_data = rooms[current_room_id]
    print(f"\n{room_data['description']}")
    # Optionally, list exits:
    exits = ", ".join(room_data["exits"].keys())
    print(f"Exits: {exits}")

def process_command(keywords):
    # This is the core of our NLP processing. It takes extracted keywords and determines the action.
    verb = None
    noun = None

    # Find the first verb and noun extracted. In a real game, you might handle multiple verbs/nouns.
    for keyword_type, keyword in keywords:
        if keyword_type == "verb" and verb is None:
            verb = keyword
        elif keyword_type == "noun" and noun is None:
            noun = keyword

    # --- Action Handling ---

    # Handle movement commands
    if verb in ["go", "move", "walk"]:
        if noun in rooms[player_state["location"]]["exits"]:
            new_location = rooms[player_state["location"]]["exits"][noun]
            player_state["location"] = new_location
            display_location() # Show the new location's description
        else:
            print("You can't go that way.")

    # Handle looking/examining commands
    elif verb in ["look", "examine"]:
        if noun == "room" or noun is None: # Default to looking at the room if no specific noun
            display_location()
        elif noun == "object" and player_state["location"] == "clearing":
            print("The object is a glowing, ancient amulet. It hums with faint energy.")
        else:
            print("You don't see that here to examine.")

    # Handle taking/getting commands
    elif verb in ["take", "get", "pick"]:
        if noun == "object" and player_state["location"] == "clearing":
            if "amulet" not in player_state["inventory"]: # Prevent taking multiple times
                print("You carefully pick up the amulet. It feels warm in your hand.")
                player_state["inventory"].append("amulet")
            else:
                print("You already have the amulet.")
        else:
            print("You can't take that.")

    # Handle unknown commands
    else:
        print("I don't understand that command.")

# --- Game Loop ---

def play_game():
    print("Welcome to the Text Adventure!")
    print("Type 'quit' to exit the game.")
    display_location() # Show the starting location

    while True: # The main game loop
        command = input("\n> ") # Prompt the player for input

        if command.lower() == "quit":
            print("Thanks for playing!")
            break # Exit the loop

        keywords = get_keywords(command) # Get keywords from the player's command
        if keywords: # Only process if we found any keywords
            process_command(keywords)
        else:
            print("Please say something more specific.")

# --- Example Usage ---
if __name__ == "__main__":
    # This block ensures play_game() runs only when the script is executed directly.
    play_game()

# Example commands you can try:
# go north
# move east
# look
# examine object
# take amulet
# walk south
# get item