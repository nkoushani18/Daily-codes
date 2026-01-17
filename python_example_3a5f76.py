# Objective: Learn to generate unique abstract art using Python's Pillow library and simple random manipulations.
# This tutorial focuses on basic image creation, color manipulation, and applying random transformations.

# Import the Pillow library, which is a fork of the Python Imaging Library (PIL)
# and is essential for image manipulation in Python.
from PIL import Image, ImageDraw
import random

# --- Configuration ---
# Define the dimensions of our canvas. This determines the width and height of the artwork.
WIDTH = 800
HEIGHT = 600

# Define the number of shapes to draw. More shapes generally lead to more complex art.
NUM_SHAPES = 150

# Define the maximum size for random shapes. This controls the scale of individual elements.
MAX_SHAPE_SIZE = 100

# --- Helper Functions ---

# This function generates a random color.
# It returns an RGB tuple (Red, Green, Blue) where each value is between 0 and 255.
def generate_random_color():
    # random.randint(a, b) returns a random integer N such that a <= N <= b.
    # We generate random values for red, green, and blue components.
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # The RGB tuple is returned. This format is understood by Pillow for colors.
    return (r, g, b)

# This function generates a random coordinate within the canvas dimensions.
# It ensures that the generated x and y values are within the bounds of our image.
def generate_random_position(max_width, max_height):
    # Generate a random x-coordinate from 0 to max_width - 1.
    x = random.randint(0, max_width - 1)
    # Generate a random y-coordinate from 0 to max_height - 1.
    y = random.randint(0, max_height - 1)
    # Return the (x, y) coordinate tuple.
    return (x, y)

# This function generates a random size for a shape.
# It ensures the size is not too small or too large, providing some variety.
def generate_random_size(max_size):
    # Generate a random size between 10 (to ensure visibility) and max_size.
    return random.randint(10, max_size)

# --- Main Art Generation Function ---

# This function orchestrates the creation of our abstract artwork.
def create_abstract_art():
    # Create a new blank image with the specified WIDTH and HEIGHT.
    # 'RGB' mode means it's a color image with Red, Green, and Blue channels.
    # (255, 255, 255) sets the initial background color to white.
    image = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))

    # Get a drawing context. This object allows us to draw shapes and lines onto the image.
    draw = ImageDraw.Draw(image)

    # Loop NUM_SHAPES times to draw multiple elements on the canvas.
    for _ in range(NUM_SHAPES):
        # Determine the type of shape to draw randomly.
        # We have a few simple shapes for variety: ellipses and rectangles.
        shape_type = random.choice(['ellipse', 'rectangle'])

        # Generate random parameters for the shape.
        # Position of the top-left corner of the bounding box for the shape.
        pos1 = generate_random_position(WIDTH, HEIGHT)
        # Size of the shape. This will be used to calculate the second corner.
        size = generate_random_size(MAX_SHAPE_SIZE)

        # Calculate the second position (bottom-right corner of the bounding box).
        # We add the size to the first position.
        pos2 = (pos1[0] + size, pos1[1] + size)

        # Generate a random fill color for the shape.
        fill_color = generate_random_color()

        # Draw the shape onto the image.
        if shape_type == 'ellipse':
            # draw.ellipse() takes a bounding box [x0, y0, x1, y1] and fill color.
            # The bounding box defines the rectangle within which the ellipse is inscribed.
            draw.ellipse([pos1[0], pos1[1], pos2[0], pos2[1]], fill=fill_color)
        elif shape_type == 'rectangle':
            # draw.rectangle() also takes a bounding box and fill color.
            draw.rectangle([pos1[0], pos1[1], pos2[0], pos2[1]], fill=fill_color)

    # Return the generated image object.
    return image

# --- Example Usage ---

# This block of code runs only when the script is executed directly (not imported as a module).
if __name__ == "__main__":
    print("Generating abstract art...")
    # Call the function to create the artwork.
    generated_art = create_abstract_art()

    # Save the generated image to a file.
    # The filename includes a random component to ensure uniqueness if run multiple times.
    filename = f"abstract_art_{random.randint(1000, 9999)}.png"
    generated_art.save(filename)

    print(f"Art saved as: {filename}")
    print("Open the file to view your unique creation!")
    # You can optionally display the image directly if you have a viewer configured.
    # generated_art.show()