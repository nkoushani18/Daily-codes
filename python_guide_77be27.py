# Fractal Tree Visualization with Python Turtle and Recursion

# Learning Objective:
# This tutorial will teach you how to visualize fractal patterns, specifically a
# fractal tree, using Python's Turtle graphics library and the concept of recursion.
# You will learn:
# 1. How to use the Python Turtle module for basic drawing.
# 2. The fundamental concept of recursion: a function calling itself.
# 3. How recursion can be used to create complex, self-similar patterns.
# 4. How to control the depth and angle of a fractal to observe its behavior.

import turtle
import random

# --- Configuration ---
# Define the screen dimensions.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BACKGROUND_COLOR = "lightgreen"
PEN_COLOR = "brown"
MAX_RECURSION_DEPTH = 10
INITIAL_BRANCH_LENGTH = 100
MIN_BRANCH_LENGTH_FACTOR = 0.7  # How much shorter branches get each recursion
ANGLE_DEGREES = 30
BRANCH_WIDTH_INITIAL = 10
WIDTH_DECREASE_FACTOR = 0.7

# --- Fractal Tree Drawing Function ---
def draw_fractal_tree(t, branch_length, level, max_level, angle, width):
    """
    Recursively draws a fractal tree.

    Args:
        t (turtle.Turtle): The Turtle object used for drawing.
        branch_length (float): The current length of the branch to draw.
        level (int): The current recursion depth.
        max_level (int): The maximum allowed recursion depth.
        angle (float): The angle (in degrees) to turn for branches.
        width (float): The current width of the pen for drawing.
    """
    # Base Case: If we've reached the maximum recursion depth or the branch is too short, stop.
    # This is crucial for preventing infinite recursion.
    if level > max_level or branch_length < 5: # Added a minimum length to stop drawing tiny branches
        return

    # Set the pen size for the current branch.
    t.pensize(width)
    # Set the color for the current branch.
    t.pencolor(PEN_COLOR)

    # Draw the current branch.
    t.forward(branch_length)

    # --- Recursive Steps ---
    # Save the current position and heading. This is important because we'll
    # be moving the turtle, and we need to return to this point to draw
    # the other branches.
    current_pos = t.pos()
    current_heading = t.heading()

    # 1. Draw the right branch:
    # Turn right by the specified angle.
    t.right(angle)
    # Calculate the length of the next branch. It's shorter than the current one.
    next_branch_length = branch_length * MIN_BRANCH_LENGTH_FACTOR
    # Calculate the width of the next branch.
    next_width = width * WIDTH_DECREASE_FACTOR
    # Recursively call draw_fractal_tree for the right branch, increasing the level.
    draw_fractal_tree(t, next_branch_length, level + 1, max_level, angle, next_width)

    # Restore the position and heading to draw the left branch from the same point.
    t.penup() # Lift the pen to avoid drawing a line while returning
    t.goto(current_pos)
    t.setheading(current_heading)
    t.pendown() # Put the pen down to continue drawing

    # 2. Draw the left branch:
    # Turn left by the specified angle.
    t.left(angle)
    # Recursively call draw_fractal_tree for the left branch, increasing the level.
    # We reuse the calculated next_branch_length and next_width.
    draw_fractal_tree(t, next_branch_length, level + 1, max_level, angle, next_width)

    # Restore the position and heading after drawing both branches from this point.
    # This allows the parent call to continue drawing its other branches correctly.
    t.penup()
    t.goto(current_pos)
    t.setheading(current_heading)
    t.pendown()

# --- Main Execution ---
if __name__ == "__main__":
    # Set up the screen.
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Fractal Tree Explorer")

    # Create a Turtle object for drawing.
    tree_turtle = turtle.Turtle()
    tree_turtle.speed(0)  # Set speed to fastest (0).
    tree_turtle.hideturtle() # Hide the turtle icon while drawing.

    # Position the turtle at the bottom center to start drawing the tree trunk.
    tree_turtle.penup()
    tree_turtle.goto(0, -SCREEN_HEIGHT / 2 + 50) # Move up a bit from the very bottom
    tree_turtle.pendown()
    tree_turtle.left(90) # Point the turtle upwards to draw the trunk.

    # --- Example Usage ---
    print("Drawing a fractal tree...")
    # Initiate the fractal tree drawing process.
    # We start at level 0, with the initial branch length and width.
    draw_fractal_tree(
        tree_turtle,
        INITIAL_BRANCH_LENGTH,
        0, # current level
        MAX_RECURSION_DEPTH,
        ANGLE_DEGREES,
        BRANCH_WIDTH_INITIAL
    )

    # Keep the window open until it's manually closed.
    screen.mainloop()
    print("Fractal tree drawing complete.")