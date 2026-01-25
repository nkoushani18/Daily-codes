# Fractal Generation with Turtle Graphics - A Recursive Approach

# Learning Objective:
# This tutorial will teach you how to procedurally generate and visualize
# intricate fractal art using Python's turtle graphics library. We will focus
# on the concept of recursion to create self-similar patterns, a fundamental
# principle in fractal generation. By the end of this tutorial, you will
# understand how simple rules and recursive calls can lead to complex and
# beautiful geometric designs.

import turtle

# --- Fractal Generation Function ---

# This function recursively draws a fractal pattern.
# Recursion is when a function calls itself. It's perfect for fractals
# because fractal patterns are often defined in terms of smaller,
# identical versions of themselves.
def draw_fractal(artist, length, depth, angle):
    """
    Recursively draws a fractal pattern.

    Args:
        artist: The turtle object used for drawing.
        length: The current length of the line segment to draw.
        depth: The current recursion depth. This controls how many times
               the fractal pattern repeats.
        angle: The angle to turn for creating branches.
    """
    # Base Case: The condition that stops the recursion.
    # If the depth reaches 0, we stop drawing further. This prevents
    # infinite recursion and defines the smallest element of our fractal.
    if depth == 0:
        artist.forward(length)
        return  # Exit the function to stop recursion for this branch.

    # Recursive Step: The part where the function calls itself.
    # We reduce the length and depth for the next level of recursion.
    # This is how we create smaller, self-similar versions of the pattern.

    # Calculate the new length for the next level of recursion.
    # We typically reduce the length to make the fractal smaller as we go deeper.
    new_length = length / 2

    # Draw the first branch.
    draw_fractal(artist, new_length, depth - 1, angle)

    # Turn left to prepare for the next branch.
    # This angle is crucial for shaping the fractal.
    artist.left(angle)

    # Draw the second branch.
    draw_fractal(artist, new_length, depth - 1, angle)

    # Turn right to return to the original orientation before drawing the previous branch.
    # This allows us to draw subsequent branches from the correct position and angle.
    artist.right(angle)
    # We need to account for the 'left' turn made earlier.
    artist.right(angle) # This is because we turned left and then right.

    # Draw the third branch.
    draw_fractal(artist, new_length, depth - 1, angle)

    # Turn left to return to the original orientation after drawing the third branch.
    artist.left(angle)


# --- Setup and Execution ---

# This is the main part of our script where we set up the turtle and
# initiate the fractal drawing.

def create_fractal_art(initial_length=100, recursion_depth=5, turn_angle=30):
    """
    Sets up the turtle screen and draws a fractal.

    Args:
        initial_length: The starting length of the main branch.
        recursion_depth: The maximum depth of recursion for the fractal.
        turn_angle: The angle used for branching.
    """
    # Create a screen object to control the drawing window.
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  # Set the dimensions of the window.
    screen.bgcolor("black")  # Set the background color to black.
    screen.title("Recursive Fractal Art")  # Set the window title.

    # Create a turtle object, which is our "artist".
    artist = turtle.Turtle()
    artist.speed(0)  # Set the drawing speed to the fastest possible.
    artist.color("cyan")  # Set the color of the drawn lines.
    artist.penup()  # Lift the pen so we don't draw while moving to the start.
    artist.goto(0, -200)  # Move the turtle to the starting position at the bottom center.
    artist.pendown()  # Put the pen down to start drawing.
    artist.left(90)  # Point the turtle upwards initially.

    # Call the recursive function to start drawing the fractal.
    # We pass the turtle object, initial length, depth, and angle.
    draw_fractal(artist, initial_length, recursion_depth, turn_angle)

    # Hide the turtle cursor after drawing is complete for a cleaner look.
    artist.hideturtle()

    # Keep the window open until it's manually closed.
    screen.mainloop()

# --- Example Usage ---

# This is how you can run the fractal generation.
# You can experiment with different values for the parameters
# to create unique fractal patterns.

if __name__ == "__main__":
    print("Generating fractal art...")
    # Example 1: A standard fractal with medium depth and angle.
    create_fractal_art(initial_length=150, recursion_depth=4, turn_angle=45)

    # Example 2: A more complex fractal with higher depth.
    # Uncomment the line below to try it out.
    # create_fractal_art(initial_length=80, recursion_depth=6, turn_angle=30)

    # Example 3: A fractal with a wider angle for more spread.
    # Uncomment the line below to try it out.
    # create_fractal_art(initial_length=120, recursion_depth=3, turn_angle=60)
    print("Fractal generation complete. Window should be visible.")