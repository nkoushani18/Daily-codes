"""
Educational Tutorial: Building a Simple Chatbot That Learns from Conversations

This tutorial will guide you through the process of creating a basic Python chatbot.
The core concept we'll focus on is how a chatbot can *learn* by remembering
previous interactions and using that knowledge to generate more relevant responses
in the future. We will achieve this by storing a simple knowledge base of
user input and bot responses.

Learning Objectives:
1. Understand how to store conversational data.
2. Implement a basic logic for generating responses based on learned data.
3. Learn how to update the chatbot's knowledge base.
4. See a practical example of a learning chatbot in action.
"""

import random # We'll use this to pick a random response if no specific one is found

class LearningChatbot:
    """
    A rudimentary chatbot that learns from user input and adapts its responses.

    This chatbot uses a simple dictionary to store pairs of user inputs and
    corresponding bot responses. When the user says something new, the bot
    asks for a response and stores this new pair, effectively "learning".
    """

    def __init__(self):
        """
        Initializes the chatbot.

        We create an empty dictionary `knowledge_base` to store our learned
        conversations. The keys will be the user's input (what they said),
        and the values will be a list of possible responses the bot can give.
        Storing responses in a list allows for variation.
        """
        self.knowledge_base = {}

    def get_response(self, user_input):
        """
        Retrieves a response from the chatbot.

        Args:
            user_input (str): The message from the user.

        Returns:
            str: The chatbot's response.
        """
        # First, we convert the user's input to lowercase. This makes our
        # learning case-insensitive, so "Hello" and "hello" are treated the same.
        user_input_lower = user_input.lower()

        # We check if the chatbot has encountered this specific input before.
        if user_input_lower in self.knowledge_base:
            # If we have seen this input, we have a list of pre-defined responses.
            # We randomly pick one from the list to make the conversation more dynamic.
            # `random.choice()` is perfect for this.
            possible_responses = self.knowledge_base[user_input_lower]
            return random.choice(possible_responses)
        else:
            # If this is a new input, we don't know how to respond yet.
            # We'll prompt the user to teach us.
            return "I don't know how to respond to that. What should I say?"

    def learn(self, user_input, bot_response):
        """
        Learns a new response from the user.

        Args:
            user_input (str): The user's original input.
            bot_response (str): The desired response from the bot.
        """
        # Again, we standardize the user input to lowercase for consistency.
        user_input_lower = user_input.lower()

        # If the input is already in our knowledge base, we want to add the
        # new response to the existing list of possibilities, rather than
        # overwriting it. This enriches our learning.
        if user_input_lower in self.knowledge_base:
            # We check if this specific response is already known for this input.
            # This avoids duplicate entries of the exact same response.
            if bot_response not in self.knowledge_base[user_input_lower]:
                self.knowledge_base[user_input_lower].append(bot_response)
                print(f"Learned to respond '{bot_response}' to '{user_input}'.")
            else:
                print(f"I already know how to respond '{bot_response}' to '{user_input}'.")
        else:
            # If it's a completely new input, we create a new entry in our
            # knowledge base. The value is a list containing the single new response.
            self.knowledge_base[user_input_lower] = [bot_response]
            print(f"Learned to respond '{bot_response}' to '{user_input}'.")

# --- Example Usage ---

def start_conversation(chatbot):
    """
    Starts an interactive conversation with the learning chatbot.
    """
    print("Hello! I'm your learning chatbot. Type 'quit' to exit.")

    while True:
        user_message = input("You: ") # Get input from the user

        if user_message.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break # Exit the loop if the user types 'quit'

        # Get a response from the chatbot
        bot_reply = chatbot.get_response(user_message)

        print(f"Chatbot: {bot_reply}")

        # If the chatbot didn't know how to respond, it asked for one.
        # We then need to capture that desired response and teach the bot.
        if "What should I say?" in bot_reply:
            new_response = input("Teach me: ") # Get the desired response from the user
            chatbot.learn(user_message, new_response) # Teach the bot

if __name__ == "__main__":
    # This is a common Python idiom. It means the code inside this block
    # will only run when the script is executed directly (not when imported
    # as a module into another script).

    my_chatbot = LearningChatbot() # Create an instance of our chatbot

    # Let's give the chatbot a few initial things to know
    my_chatbot.learn("hello", "Hi there!")
    my_chatbot.learn("how are you", "I'm a bot, so I don't have feelings, but thanks for asking!")
    my_chatbot.learn("what is your name", "I am a simple learning chatbot.")
    my_chatbot.learn("hello", "Hello!") # Adding another response for "hello"

    # Start the interactive conversation
    start_conversation(my_chatbot)