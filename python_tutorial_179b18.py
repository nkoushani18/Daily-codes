# --- Educational Chatbot Tutorial: Learning with Dictionaries ---
#
# Objective: This tutorial will teach you how to build a simple text-based
# chatbot that learns and responds to user input by storing and retrieving
# information using Python dictionaries. We will focus on how dictionaries
# can be used to map user "inputs" to bot "responses."
#
# Concepts Covered:
# - Python Dictionaries: Storing key-value pairs.
# - Basic Input/Output: Getting user input and printing bot responses.
# - Conditional Logic: Using if/else statements to control bot behavior.
# - Looping: Keeping the conversation going until the user quits.
# - String Manipulation: Basic text processing.
#
#----------------------------------------------------------------------

# Initialize an empty dictionary to store our learned knowledge.
# This dictionary will act as the chatbot's "memory."
# Keys will be user inputs (what the user says), and values will be the
# chatbot's programmed responses to those inputs.
chatbot_knowledge = {}

def get_bot_response(user_input):
    """
    This function determines the chatbot's response based on user input.
    It first checks if the chatbot "knows" a response to the user's input.
    If it does, it returns the learned response.
    If not, it prompts the user to teach the chatbot.

    Args:
        user_input (str): The message from the user.

    Returns:
        str: The chatbot's response.
    """
    # Convert user input to lowercase for case-insensitive matching.
    # This makes the chatbot more forgiving; "Hello" and "hello" will be treated the same.
    processed_input = user_input.lower()

    # Check if the processed input exists as a key in our chatbot_knowledge dictionary.
    if processed_input in chatbot_knowledge:
        # If the key exists, retrieve and return the corresponding value (the learned response).
        return chatbot_knowledge[processed_input]
    else:
        # If the input is not in our knowledge base, we need to ask the user to teach us.
        return "I don't know how to respond to that. What should I say?"

def teach_chatbot(user_input, bot_response):
    """
    This function adds a new piece of knowledge to the chatbot's memory.
    It takes the user's original input and the desired bot response,
    and stores them as a key-value pair in the chatbot_knowledge dictionary.

    Args:
        user_input (str): The original user input that triggered the learning.
        bot_response (str): The response the user wants the bot to give for that input.
    """
    # Convert the user's input to lowercase to ensure consistent learning.
    processed_input = user_input.lower()

    # Add the new key-value pair to the dictionary.
    # The user's input becomes the key, and the bot's desired response becomes the value.
    chatbot_knowledge[processed_input] = bot_response
    print("Thank you! I've learned that.")

def start_chat():
    """
    This function starts the main chat loop.
    It continuously prompts the user for input, gets a response from the bot,
    and handles learning new responses when the bot doesn't know.
    """
    print("Hello! I'm a simple chatbot that learns. Type 'quit' to exit.")

    # Start an infinite loop to keep the conversation going.
    while True:
        # Get input from the user. The input() function pauses the program
        # and waits for the user to type something and press Enter.
        user_message = input("You: ")

        # Check if the user wants to quit the conversation.
        if user_message.lower() == 'quit':
            print("Bot: Goodbye!")
            break # Exit the while loop, ending the chat.

        # Get the bot's initial response using the knowledge we have.
        bot_reply = get_bot_response(user_message)

        # If the bot's reply indicates it needs to learn, handle the learning process.
        if "What should I say?" in bot_reply:
            print(f"Bot: {bot_reply}")
            # Prompt the user for the correct response.
            new_response = input("Bot: ")
            # Teach the chatbot the new input-response pair.
            teach_chatbot(user_message, new_response)
        else:
            # If the bot knows the answer, just print its learned response.
            print(f"Bot: {bot_reply}")

# --- Example Usage ---
# To run this code:
# 1. Save it as a Python file (e.g., learning_chatbot.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using: python learning_chatbot.py

# The 'if __name__ == "__main__":' block ensures that the start_chat() function
# is called only when the script is executed directly (not when it's imported
# as a module into another script). This is a standard Python best practice.
if __name__ == "__main__":
    start_chat()

# After running, try these interactions:
# You: hello
# Bot: I don't know how to respond to that. What should I say?
# Bot: Hi there!
# Thank you! I've learned that.
# You: hello
# Bot: Hi there!
#
# You: how are you
# Bot: I don't know how to respond to that. What should I say?
# Bot: I'm a bot, so I don't have feelings!
# Thank you! I've learned that.
# You: how are you
# Bot: I'm a bot, so I don't have feelings!
#
# You: quit
# Bot: Goodbye!