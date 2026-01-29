# Learning Objective:
# This tutorial will teach you how to generate and manipulate
# simple ASCII art in Python using user input for customization.
# We'll focus on the concept of string manipulation and basic loops
# to create dynamic visual output.

# Import necessary modules (though none are strictly needed for this basic example)
# import random # We might use this later for more advanced art!

def create_ascii_box(width, height, char='*'):
    """
    Generates a simple rectangular ASCII art box.

    Args:
        width (int): The desired width of the box (number of characters).
        height (int): The desired height of the box (number of lines).
        char (str, optional): The character to use for drawing the box.
                              Defaults to '*'.

    Returns:
        str: A multi-line string representing the ASCII box.
    """
    # Input validation: Ensure width and height are positive integers.
    # This prevents errors and makes the function more robust.
    if not isinstance(width, int) or width <= 0:
        print("Error: Width must be a positive integer.")
        return "" # Return an empty string to indicate an error.
    if not isinstance(height, int) or height <= 0:
        print("Error: Height must be a positive integer.")
        return ""

    # Create the top and bottom borders of the box.
    # A border is simply a line of 'char' repeated 'width' times.
    top_bottom_border = char * width

    # Create the middle rows of the box.
    # Each middle row consists of the 'char' at the beginning,
    # followed by spaces for the inside, and then the 'char' at the end.
    # The number of spaces is the width minus 2 (for the two border characters).
    # We need to handle cases where width is 1 or 2 carefully to avoid negative spaces.
    if width > 1:
        middle_row_content = char + ' ' * (width - 2) + char
    else: # If width is 1, the middle row is just the character itself.
        middle_row_content = char

    # Now, construct the full box.
    # It starts with the top border.
    ascii_art = top_bottom_border + '\n'

    # Then, add the middle rows. We loop 'height - 2' times for these.
    # This is because the top and bottom borders account for 2 lines of height.
    for _ in range(height - 2):
        ascii_art += middle_row_content + '\n'

    # Finally, add the bottom border.
    # We only add the bottom border if the height is greater than 1.
    # If height is 1, the top border is also the bottom border.
    if height > 1:
        ascii_art += top_bottom_border

    return ascii_art

def get_user_input():
    """
    Prompts the user for input to customize the ASCII art.

    Returns:
        tuple: A tuple containing (width, height, char).
               Returns (None, None, None) if input is invalid.
    """
    try:
        # Get width from user. int() converts the input string to an integer.
        width_str = input("Enter the desired width of the box: ")
        width = int(width_str)

        # Get height from user.
        height_str = input("Enter the desired height of the box: ")
        height = int(height_str)

        # Get the character for drawing.
        # We expect a single character. If more is entered, we take the first one.
        char = input("Enter the character to use for drawing (e.g., #, -, =): ")
        if not char: # If the user presses Enter without typing anything
            char = '*' # Use a default character

        # Return the collected values.
        return width, height, char

    except ValueError:
        # This exception occurs if int() cannot convert the input string to an integer.
        print("Invalid input! Please enter numbers for width and height.")
        return None, None, None # Indicate an error by returning None values.

# --- Main part of the program ---
if __name__ == "__main__":
    # This block of code runs only when the script is executed directly
    # (not when it's imported as a module into another script).

    print("--- ASCII Art Box Generator ---")

    # Get customization options from the user.
    user_width, user_height, user_char = get_user_input()

    # Check if the user input was valid before proceeding.
    if user_width is not None and user_height is not None and user_char is not None:
        # Generate the ASCII art using the user's input.
        generated_art = create_ascii_box(user_width, user_height, user_char)

        # Display the generated ASCII art if it was created successfully.
        if generated_art:
            print("\nHere is your custom ASCII art box:")
            print(generated_art)
        # If generated_art is empty, it means create_ascii_box already printed an error.

    print("\n--- Program Finished ---")

# Example Usage:
# When you run this script, it will ask you for input.
#
# Example 1:
# Enter the desired width of the box: 10
# Enter the desired height of the box: 5
# Enter the character to use for drawing (e.g., #, -, =): #
#
# Output will be:
#
# Here is your custom ASCII art box:
# ##########
# #        #
# #        #
# #        #
# ##########
#
# Example 2 (invalid input):
# Enter the desired width of the box: abc
# Invalid input! Please enter numbers for width and height.
#
# --- Program Finished ---
#
# Example 3 (small box):
# Enter the desired width of the box: 2
# Enter the desired height of the box: 2
# Enter the character to use for drawing (e.g., #, -, =): -
#
# Output will be:
#
# Here is your custom ASCII art box:
# --
# --
#
# --- Program Finished ---
#
# Example 4 (single character width):
# Enter the desired width of the box: 1
# Enter the desired height of the box: 3
# Enter the character to use for drawing (e.g., #, -, =): |
#
# Output will be:
#
# Here is your custom ASCII art box:
# |
# |
# |
#
# --- Program Finished ---