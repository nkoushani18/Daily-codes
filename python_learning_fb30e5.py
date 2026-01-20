# AI Pet Tutorial: Basic Learning with Dictionaries

# Objective:
# This tutorial will teach you how to create a simple text-based AI pet in Python
# that learns and reacts to your commands. We'll focus on using dictionaries
# to store and retrieve information, simulating a basic form of AI memory.

# We'll learn how to:
# 1. Represent the pet's state (e.g., mood, hunger).
# 2. Define commands the user can give.
# 3. Make the pet "learn" new commands and their corresponding actions.
# 4. Have the pet react to known commands.

# Let's start by defining our pet's initial state.
# We'll use a dictionary to hold its properties.
pet_state = {
    "name": "Buddy",
    "mood": "happy",
    "hunger": 5, # 0 is full, 10 is starving
    "energy": 8  # 0 is exhausted, 10 is full of energy
}

# This dictionary stores the commands the pet knows and how to respond.
# The keys are the commands (strings), and the values are the responses (strings).
# This is our pet's "knowledge base" or "memory".
known_commands = {
    "hello": "Hi there!",
    "how are you": "I'm feeling great!",
    "sleep": "Zzzzz...",
    "play": "Let's play fetch!",
    "eat": "Yum, I love food!"
}

# --- Functions to manage the pet ---

def display_pet_status(pet):
    """
    Prints the current status of the pet.
    This helps the user understand how the pet is feeling.
    """
    print(f"\n--- {pet['name']} Status ---")
    print(f"Mood: {pet['mood'].capitalize()}") # Capitalize the first letter for better readability
    print(f"Hunger: {pet['hunger']}/10")
    print(f"Energy: {pet['energy']}/10")
    print("--------------------")

def process_command(command, pet, knowledge_base):
    """
    Processes a user's command and updates the pet's state or provides a response.
    This is the core of our AI's interaction logic.
    """
    command = command.lower().strip() # Normalize the command: lowercase and remove whitespace

    # Check if the pet knows this command
    if command in knowledge_base:
        response = knowledge_base[command]
        print(f"{pet['name']} says: {response}")

        # --- Simple state changes based on commands ---
        # These are basic examples of how commands can affect the pet's internal state.
        if command == "play":
            pet["hunger"] += 1  # Playing makes the pet hungrier
            pet["energy"] -= 2  # Playing uses energy
            pet["mood"] = "excited"
        elif command == "eat":
            pet["hunger"] -= 3  # Eating reduces hunger
            pet["energy"] += 1  # Eating gives some energy
            pet["mood"] = "satisfied"
        elif command == "sleep":
            pet["energy"] += 4  # Sleeping restores energy
            pet["mood"] = "sleepy"
        elif command == "hello" or command == "how are you":
            pet["mood"] = "happy"

        # Ensure state values stay within reasonable bounds
        pet["hunger"] = max(0, min(10, pet["hunger"]))
        pet["energy"] = max(0, min(10, pet["energy"]))

    else:
        # If the pet doesn't know the command, it can "learn" it.
        # This is a simple learning mechanism.
        print(f"'{command.capitalize()}'? I don't know that. What should I do?")
        new_response = input("Tell me what to say: ").strip()

        if new_response: # Only add if the user provided a response
            knowledge_base[command] = new_response
            print(f"Okay, I've learned '{command}'! Now I'll say: '{new_response}'")
            # Optionally, you could also associate state changes with new commands here.
            # For simplicity, we're just learning the response for now.
        else:
            print("Hmm, I guess I won't learn that one then.")

def game_loop(pet, knowledge_base):
    """
    The main loop for interacting with the AI pet.
    It continuously prompts the user for commands until they choose to quit.
    """
    print(f"Welcome, {pet['name']} the AI pet!")
    print("Type 'quit' to exit.")

    while True:
        display_pet_status(pet) # Show status at the beginning of each turn
        user_input = input("What do you want to do? ").lower().strip()

        if user_input == "quit":
            print(f"Goodbye from {pet['name']}!")
            break # Exit the loop

        # Process the user's input as a command
        process_command(user_input, pet, knowledge_base)

# --- Example Usage ---

# This is where we actually run our AI pet!
# We pass our pet's state and its knowledge base to the game loop.
if __name__ == "__main__":
    # The `if __name__ == "__main__":` block ensures that this code only runs
    # when the script is executed directly (not when imported as a module).
    # This is a standard Python best practice.

    game_loop(pet_state, known_commands)

# To run this:
# 1. Save the code as a Python file (e.g., ai_pet.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: python ai_pet.py
#
# You can then interact with your pet by typing commands like:
# hello
# how are you
# play
# eat
# sleep
#
# If you type a command the pet doesn't know, it will ask you to teach it!
# For example, try typing: dance
# Then, provide a response like "I love to groove!"
# The next time you type 'dance', Buddy will respond with "I love to groove!"