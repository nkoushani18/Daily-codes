# Abstract Art Generator using Mathematical Functions and Randomness
#
# Learning Objective: This tutorial will teach you how to combine
# mathematical functions and Python's random module to generate unique
# abstract visual patterns. We will focus on using trigonometric
# functions (sine and cosine) and random color generation to create
# visually interesting and unpredictable artwork.

# Import necessary libraries
# Pillow (PIL fork) is used for image manipulation in Python.
# We'll use it to create a blank image and draw pixels on it.
from PIL import Image
# The `random` module provides functions for generating random numbers.
# This is crucial for making our art unique each time.
import random
# The `math` module provides mathematical functions like sin and cos.
# These will be the core of our abstract patterns.
import math

# --- Configuration ---
# Define the dimensions of our artwork.
# These variables allow for easy adjustment of the output size.
IMAGE_WIDTH = 800
IMAGE_HEIGHT = 600

# Define the number of "drawing points" to use.
# More points generally lead to more complex patterns.
NUM_POINTS = 15000

# Define the range for random color components (0-255 for RGB).
# This ensures we get vibrant and varied colors.
MIN_COLOR_VALUE = 0
MAX_COLOR_VALUE = 255

# --- Core Generation Logic ---

def generate_abstract_art(width, height, num_points):
    """
    Generates a unique abstract art image using mathematical functions and randomness.

    Args:
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.
        num_points (int): The number of points to plot on the image.

    Returns:
        PIL.Image.Image: A Pillow Image object representing the generated art.
    """
    # Create a new blank image with a black background.
    # 'RGB' mode means we'll be working with Red, Green, Blue color channels.
    # (0, 0, 0) is black in RGB.
    img = Image.new('RGB', (width, height), color=(0, 0, 0))
    # Get access to the image's pixel data for efficient modification.
    pixels = img.load()

    # Loop for a specified number of points to draw.
    # Each iteration will generate a new pixel with a potentially unique color and position.
    for _ in range(num_points):
        # Generate random values that will influence the position.
        # `random.uniform` gives us floating-point numbers within a range.
        # We use `width` and `height` to scale the random values to our image dimensions.
        rand_x_factor = random.uniform(0, 1)
        rand_y_factor = random.uniform(0, 1)

        # --- Mathematical Pattern Generation ---
        # This is where the abstract art "magic" happens.
        # We're using trigonometric functions (sine and cosine) which produce
        # wave-like patterns. By using random factors, we shift and scale these waves.

        # Calculate X coordinate using sine and random factors.
        # `math.sin()` returns a value between -1 and 1.
        # We multiply by `width` to map this wave across the image's width.
        # Adding `rand_x_factor * width` shifts the starting point of the wave.
        x_pos = int(width * (0.5 + 0.4 * math.sin(rand_x_factor * 10 * math.pi) + 0.1 * rand_x_factor))

        # Calculate Y coordinate using cosine and random factors.
        # `math.cos()` also returns a value between -1 and 1.
        # We multiply by `height` to map this wave across the image's height.
        # Adding `rand_y_factor * height` shifts the starting point of the wave.
        y_pos = int(height * (0.5 + 0.4 * math.cos(rand_y_factor * 10 * math.pi) + 0.1 * rand_y_factor))

        # Ensure calculated coordinates are within image bounds.
        # This is a safety measure, though the formulas are designed to stay close.
        x_pos = max(0, min(x_pos, width - 1))
        y_pos = max(0, min(y_pos, height - 1))

        # --- Random Color Generation ---
        # Create a random color for the current pixel.
        # `random.randint(a, b)` returns a random integer N such that a <= N <= b.
        r = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
        g = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
        b = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)

        # Assign the generated color to the pixel at the calculated position.
        # `pixels[x, y] = (r, g, b)` sets the color of the pixel at (x, y).
        pixels[x_pos, y_pos] = (r, g, b)

    # Return the completed image object.
    return img

# --- Example Usage ---

if __name__ == "__main__":
    # This block of code runs only when the script is executed directly (not imported).

    print("Generating abstract art...")

    # Call the function to create our artwork.
    # We pass the configured dimensions and number of points.
    artwork = generate_abstract_art(IMAGE_WIDTH, IMAGE_HEIGHT, NUM_POINTS)

    # Define a filename for saving the artwork.
    # We include a timestamp or random element to ensure unique filenames.
    # For simplicity, we'll just use a fixed name here.
    output_filename = "abstract_art_output.png"

    # Save the generated image to a file.
    # The `save()` method handles writing the image data to disk.
    artwork.save(output_filename)

    print(f"Abstract art generated and saved as '{output_filename}'!")

    # Optional: Display the image if you have a GUI environment.
    # artwork.show()