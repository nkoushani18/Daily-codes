# Fractal Art with Turtle Graphics: Exploring Recursion

# ## Learning Objective:
# This tutorial will introduce you to the concept of recursion by
# generating beautiful fractal art using Python's Turtle graphics library.
# We will focus on understanding how a function can call itself to
# create complex patterns from simple rules.

# Import the turtle module, which provides graphics capabilities.
import turtle

# --- Configuration ---
# Setting up the turtle screen and the drawing pen.
screen = turtle.Screen()
screen.setup(width=800, height=800)  # Set the window size.
screen.bgcolor("black")             # Set the background color to black for better contrast.
screen.title("Recursive Fractal Art") # Set the title of the window.

# Create a turtle object, which is our drawing pen.
pen = turtle.Turtle()
pen.speed(0) # Set the speed to the fastest (0).
pen.color("cyan") # Set the drawing color.
pen.pensize(2) # Set the thickness of the pen.
pen.hideturtle() # Hide the turtle icon itself while drawing.

# --- Recursive Function: The Sierpinski Triangle ---

# This function draws a single line segment and then recursively calls itself
# to draw smaller versions of the pattern.

def draw_sierpinski_triangle(length, depth):
    """
    Recursively draws a Sierpinski triangle.

    Args:
        length (int): The length of the current line segment to draw.
        depth (int): The current recursion depth. This controls how
                     many times the function calls itself.
    """
    # BASE CASE: This is the condition that stops the recursion.
    # If the depth reaches 0, we stop drawing further and return.
    # This prevents an infinite loop.
    if depth == 0:
        return

    # RECURSIVE STEP: This is where the magic happens.
    # The function calls itself with modified parameters to create smaller
    # versions of the pattern.

    # 1. Draw the first side of the triangle.
    pen.forward(length)

    # 2. Recursively call for the left smaller triangle.
    # We turn left by 120 degrees, draw a smaller triangle (length/2),
    # and then turn right by 120 degrees to get back to the original orientation.
    pen.left(120)
    draw_sierpinski_triangle(length / 2, depth - 1)
    pen.right(120)

    # 3. Recursively call for the right smaller triangle.
    # We move forward to the next vertex, turn right by 120 degrees,
    # draw a smaller triangle, and turn left by 120 degrees to realign.
    pen.forward(length) # Move to the next vertex
    pen.right(120)
    draw_sierpinski_triangle(length / 2, depth - 1)
    pen.left(120)

    # 4. Recursively call for the top smaller triangle.
    # We move to the top vertex, turn left by 60 degrees, draw the final
    # smaller triangle, and then turn right by 60 degrees to complete the iteration.
    pen.forward(length) # Move to the last vertex
    pen.left(60)
    draw_sierpinski_triangle(length / 2, depth - 1)
    pen.right(60)

    # Important: After drawing the three sub-triangles, we need to
    # return the pen to its starting position and orientation for the
    # parent call to continue correctly. This is achieved by moving
    # back the same distance and undoing the turns.
    # This part is crucial for the recursive structure to work.
    pen.backward(length) # Go back to the start of the current line

# --- Example Usage ---

# Set the initial starting position of the turtle.
# Moving it to the bottom-left corner of the screen, slightly up.
pen.penup() # Lift the pen so it doesn't draw while moving.
pen.goto(-150, -150) # Move to a starting coordinate.
pen.pendown() # Put the pen down to start drawing.

# Define the initial parameters for the Sierpinski triangle.
initial_length = 300 # The size of the largest triangle.
recursion_depth = 4   # How many levels of detail we want.
                       # Higher numbers create more complex fractals but take longer.

# Call the recursive function to start drawing the fractal.
print(f"Drawing Sierpinski Triangle with length={initial_length} and depth={recursion_depth}...")
draw_sierpinski_triangle(initial_length, recursion_depth)
print("Drawing complete!")

# Keep the window open until it's manually closed.
screen.mainloop()
# --- End of Tutorial ---