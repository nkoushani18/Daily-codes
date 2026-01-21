# Art Generator Reacting to User Input with Python Turtle

# Learning Objective:
# This tutorial will teach you how to create a simple art generator
# using Python's Turtle graphics that responds to user input.
# We will focus on understanding how to:
# 1. Initialize and control the Turtle screen.
# 2. Get input from the user and use it to influence drawing.
# 3. Use loops to create repetitive patterns.
# 4. Change the turtle's appearance and movement based on input.

import turtle
import random # We'll use this for some random elements later, but keep it simple for now.

# --- Setup the Turtle Screen ---
# This sets up the window where our art will be drawn.
screen = turtle.Screen()
screen.setup(width=800, height=600) # Sets the dimensions of the drawing window.
screen.bgcolor("lightblue")        # Sets the background color.
screen.title("Interactive Art Generator") # Sets the title bar text.

# --- Create the Turtle Object ---
# This is our "pen" that will draw on the screen.
artist = turtle.Turtle()
artist.shape("turtle") # Makes the cursor look like a turtle.
artist.color("green")  # Sets the initial drawing color.
artist.speed(0)        # Sets the drawing speed to the fastest (0 is fastest).

# --- Function to Draw a Square ---
# We'll create a function to draw a basic shape that we can repeat.
def draw_square(size):
    """Draws a square of a given size."""
    # The 'for' loop repeats the code inside it a specific number of times.
    # In this case, it repeats 4 times to draw the four sides of the square.
    for _ in range(4):
        artist.forward(size) # Moves the turtle forward by 'size' pixels.
        artist.right(90)     # Turns the turtle 90 degrees to the right.

# --- Function to Draw a Circle ---
def draw_circle(radius):
    """Draws a circle of a given radius."""
    artist.circle(radius) # The turtle's built-in circle drawing method.

# --- Main Drawing Logic ---
def generate_art():
    """Generates art based on user input."""

    # --- Get User Input ---
    # We ask the user for information to customize the drawing.
    shape_choice = screen.textinput("Shape Choice", "What shape would you like? (square/circle/random)")
    color_choice = screen.textinput("Color Choice", "What color would you like? (e.g., red, blue, green, yellow)")
    size_input = screen.textinput("Size", "How big should it be? (Enter a number)")

    # --- Input Validation and Conversion ---
    # It's important to check if the user's input is valid.
    try:
        size = int(size_input) # Converts the user's text input for size into a whole number.
    except (ValueError, TypeError):
        # If the input isn't a valid number, we'll use a default size.
        screen.clear() # Clear previous drawings if there was an error.
        screen.bgcolor("red") # Indicate an error with background color.
        artist.write("Invalid size input. Please restart and enter a number.", align="center", font=("Arial", 16, "normal"))
        return # Exit the function if there's an error.

    # --- Set Turtle Properties based on Input ---
    if color_choice: # If the user entered a color, use it.
        artist.color(color_choice)
    else: # Otherwise, use a default color.
        artist.color("purple")

    # --- Drawing based on Shape Choice ---
    if shape_choice and shape_choice.lower() == "square":
        # Use a loop to draw multiple squares for a more interesting pattern.
        num_shapes = screen.numinput("Number of Shapes", "How many squares?", default=5, minval=1, maxval=20)
        for _ in range(int(num_shapes)):
            draw_square(size)
            artist.penup() # Lift the pen so it doesn't draw while moving.
            artist.goto(random.randint(-300, 300), random.randint(-200, 200)) # Move to a random position.
            artist.pendown() # Put the pen down to start drawing again.

    elif shape_choice and shape_choice.lower() == "circle":
        # Draw multiple circles at random positions.
        num_shapes = screen.numinput("Number of Shapes", "How many circles?", default=5, minval=1, maxval=20)
        for _ in range(int(num_shapes)):
            draw_circle(size)
            artist.penup()
            artist.goto(random.randint(-300, 300), random.randint(-200, 200))
            artist.pendown()

    elif shape_choice and shape_choice.lower() == "random":
        # A mix of shapes for fun!
        num_shapes = screen.numinput("Number of Shapes", "How many random shapes?", default=10, minval=1, maxval=30)
        for _ in range(int(num_shapes)):
            choice = random.choice(["square", "circle"])
            if choice == "square":
                draw_square(size // 2) # Make squares a bit smaller for variety.
            else:
                draw_circle(size // 2)
            artist.penup()
            artist.goto(random.randint(-300, 300), random.randint(-200, 200))
            artist.pendown()

    else:
        # If the user enters something unexpected for the shape.
        artist.write("Invalid shape choice. Please try again.", align="center", font=("Arial", 16, "normal"))

# --- Trigger the Art Generation ---
# This is where we start the process.
generate_art()

# --- Keep the Window Open ---
# turtle.done() is essential to keep the graphics window from closing immediately
# after the drawing is finished.
turtle.done()

# --- Example Usage ---
# To run this code:
# 1. Save it as a Python file (e.g., art_generator.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: python art_generator.py
#
# The program will then prompt you for shape, color, and size.
# Enjoy creating your art!