# Abstract Visual Art Generation from Datasets using Python and PIL

# Learning Objective:
# This tutorial will teach you how to generate abstract visual art by mapping
# numerical data from a dataset to visual properties like color and position
# using Python's Pillow (PIL) library. We will focus on understanding how to
# translate data points into artistic elements, creating unique and
# visually interesting outputs.

# Import necessary libraries
from PIL import Image, ImageDraw
import random

# --- Configuration and Setup ---

# Define the dimensions of our canvas (the image we will create)
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

# Define a default background color (R, G, B tuple)
# This sets the initial "canvas" color before we draw on it.
BACKGROUND_COLOR = (20, 20, 40) # A dark, deep blue

# Define the number of shapes (or "elements") we want to draw based on our data.
# This is a simplification; in a real scenario, this might be the number of
# data points in your dataset.
NUM_ELEMENTS = 100

# Define a range for the size of our shapes.
# Smaller numbers create smaller shapes, larger numbers create larger shapes.
MIN_SHAPE_SIZE = 10
MAX_SHAPE_SIZE = 50

# Define a range for the alpha (transparency) of our shapes.
# 0 is fully transparent, 255 is fully opaque.
MIN_ALPHA = 100
MAX_ALPHA = 220

# --- Core Logic: Data to Visual Mapping ---

def generate_random_color():
    """
    Generates a random RGB color tuple.
    Each component (R, G, B) is an integer between 0 and 255.
    This function provides the "color" aspect of our art.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def map_data_to_visuals(element_index, total_elements):
    """
    This is the core of our art generation. It takes a conceptual "data point"
    (represented here by its index) and maps it to visual properties.

    In a real application, 'element_index' would be a value from your actual dataset.
    Here, we use it to introduce some randomness and variation, simulating data.

    Args:
        element_index (int): The index of the current element being processed.
                             Simulates a data point identifier.
        total_elements (int): The total number of elements. Used for scaling.

    Returns:
        tuple: A dictionary containing visual properties:
               'x', 'y': The center coordinates of the shape.
               'size': The diameter of the shape.
               'color': The RGB color tuple of the shape.
               'alpha': The transparency of the shape.
    """
    # Map element_index to x-coordinate (horizontal position)
    # We want shapes distributed across the width of the canvas.
    # Using 'element_index' with a range of 0 to 'total_elements' allows
    # us to spread things out. The modulo operator (%) ensures we don't
    # exceed the canvas width, and we add some randomness.
    x = (element_index * (CANVAS_WIDTH // total_elements) + random.randint(-20, 20)) % CANVAS_WIDTH

    # Map element_index to y-coordinate (vertical position)
    # Similar logic to x-coordinate, but for the height.
    y = (element_index * (CANVAS_HEIGHT // total_elements) + random.randint(-20, 20)) % CANVAS_HEIGHT

    # Map element_index to size
    # We use a range and add randomness to vary shape sizes.
    # Here, we are not directly mapping a data value to size, but simulating
    # variation. In a real case, a larger data value might mean a larger size.
    size = random.randint(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)

    # Generate a random color for each element.
    # This is a simple approach; we could also map data values to specific colors.
    color = generate_random_color()

    # Map element_index to alpha (transparency)
    # This adds depth and layering to our artwork.
    alpha = random.randint(MIN_ALPHA, MAX_ALPHA)

    return {
        'x': x,
        'y': y,
        'size': size,
        'color': color,
        'alpha': alpha
    }

# --- Art Generation Function ---

def generate_abstract_art(num_elements, output_filename="abstract_art.png"):
    """
    Generates abstract visual art based on the number of elements.

    Args:
        num_elements (int): The number of elements (shapes) to draw.
        output_filename (str): The name of the file to save the art to.
    """
    # Create a new blank image with the specified dimensions and background color.
    # 'RGB' mode is for color images.
    image = Image.new('RGB', (CANVAS_WIDTH, CANVAS_HEIGHT), BACKGROUND_COLOR)

    # Get a drawing context. This object allows us to draw shapes, lines, and text.
    draw = ImageDraw.Draw(image, 'RGBA') # 'RGBA' allows for transparency

    # Loop through each conceptual "data point" (represented by an index)
    for i in range(num_elements):
        # Get the visual properties mapped from our simulated data
        visual_props = map_data_to_visuals(i, num_elements)

        # Extract the properties for easier access
        x = visual_props['x']
        y = visual_props['y']
        size = visual_props['size']
        color = visual_props['color']
        alpha = visual_props['alpha']

        # Calculate the bounding box for the ellipse (circle)
        # The 'ellipse' function takes the coordinates of a rectangle
        # defining its boundaries.
        # (x0, y0) is the top-left corner, (x1, y1) is the bottom-right.
        x0 = x - size // 2
        y0 = y - size // 2
        x1 = x + size // 2
        y1 = y + size // 2
        bounding_box = (x0, y0, x1, y1)

        # Draw an ellipse (which appears as a circle if the bounding box is square)
        # We combine the color and alpha into a RGBA tuple for transparency.
        # alpha is a value from 0 to 255, so we need to combine it with the RGB.
        # PIL handles this combination when drawing with RGBA mode.
        draw.ellipse(bounding_box, fill=(color[0], color[1], color[2], alpha))

    # Save the generated image to a file
    image.save(output_filename)
    print(f"Abstract art saved to {output_filename}")

# --- Example Usage ---

if __name__ == "__main__":
    # This block runs only when the script is executed directly.
    # It's good practice for organizing executable code.

    # Generate art with 150 elements and save it as "my_artwork.png"
    generate_abstract_art(num_elements=150, output_filename="my_artwork.png")

    # Generate a second piece with more elements for a denser look
    generate_abstract_art(num_elements=250, output_filename="dense_artwork.png")

    # Generate a third piece with fewer elements for a sparser look
    generate_abstract_art(num_elements=75, output_filename="sparse_artwork.png")