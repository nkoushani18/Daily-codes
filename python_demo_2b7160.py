# Learning Objective:
# This tutorial will teach you how to generate beautiful fractal art using
# the power of recursion and basic image manipulation in Python.
# We will focus on the Sierpinski Triangle as a clear example to understand
# how recursive functions can create complex patterns from simple rules.

# Import necessary libraries for image creation and manipulation.
# Pillow (PIL Fork) is a powerful image processing library.
# If you don't have it, install it with: pip install Pillow
from PIL import Image, ImageDraw

# --- Fractal Generation Function ---

def draw_sierpinski_triangle(draw, point1, point2, point3, level):
    """
    Recursively draws the Sierpinski Triangle.

    Args:
        draw: A PIL.ImageDraw.Draw object to draw on.
        point1, point2, point3: Tuples representing the (x, y) coordinates of the
                                 three vertices of the current triangle.
        level: The current recursion depth. This determines how many
               sub-triangles will be drawn.
    """
    # Base Case: If the recursion level reaches 0, we stop drawing.
    # This prevents infinite recursion and defines the smallest triangles.
    if level <= 0:
        # Draw a filled triangle at the current level.
        # The color is a shade of blue, making the fractal visually appealing.
        # The color value increases with recursion depth for a subtle gradient effect.
        color = (50 + (level % 5) * 10, 50 + (level % 5) * 10, 255 - (level % 5) * 10)
        draw.polygon([point1, point2, point3], fill=color)
        return # Exit the function for this branch of recursion

    # Recursive Step: If level > 0, we need to draw smaller triangles.
    # The Sierpinski Triangle is formed by connecting the midpoints of the
    # sides of the larger triangle. This creates three new, smaller triangles.

    # Calculate the midpoints of each side.
    # Midpoint formula: ((x1 + x2) / 2, (y1 + y2) / 2)
    mid12 = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)
    mid23 = ((point2[0] + point3[0]) / 2, (point2[1] + point3[1]) / 2)
    mid31 = ((point3[0] + point1[0]) / 2, (point3[1] + point1[1]) / 2)

    # Recursively call the function for each of the three new triangles.
    # We decrease the 'level' by 1 for each recursive call. This ensures
    # that each subsequent triangle is smaller and the recursion eventually ends.

    # Draw the top-left smaller triangle.
    draw_sierpinski_triangle(draw, point1, mid12, mid31, level - 1)

    # Draw the bottom-left smaller triangle.
    draw_sierpinski_triangle(draw, mid12, point2, mid23, level - 1)

    # Draw the top-right smaller triangle.
    draw_sierpinski_triangle(draw, mid31, mid23, point3, level - 1)

    # Note: The central inverted triangle is intentionally left empty.
    # This is the defining characteristic of the Sierpinski Triangle.

# --- Image Creation and Saving ---

def create_fractal_image(width, height, max_level):
    """
    Creates an image and draws the Sierpinski Triangle on it.

    Args:
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.
        max_level (int): The maximum recursion depth for the Sierpinski Triangle.
    """
    # Create a new blank image with a white background.
    # 'RGB' mode means Red, Green, Blue color channels.
    img = Image.new('RGB', (width, height), color='white')
    # Create a drawing object that can be used to draw shapes on the image.
    draw = ImageDraw.Draw(img)

    # Define the initial vertices of the main triangle.
    # These are placed in the center of the image for good composition.
    # The bottom vertices are spaced out, and the top vertex is centered above.
    # We add some padding to ensure the fractal fits within the image boundaries.
    padding = 50
    initial_point1 = (padding, height - padding)  # Bottom-left
    initial_point2 = (width - padding, height - padding) # Bottom-right
    initial_point3 = (width / 2, padding)           # Top-center

    # Start the recursive drawing process.
    draw_sierpinski_triangle(draw, initial_point1, initial_point2, initial_point3, max_level)

    # Save the generated fractal image.
    # The filename includes the max_level to distinguish different creations.
    filename = f"sierpinski_triangle_level_{max_level}.png"
    img.save(filename)
    print(f"Fractal image saved as {filename}")

# --- Example Usage ---
if __name__ == "__main__":
    # Define the desired dimensions of the output image.
    image_width = 800
    image_height = 600

    # Define the complexity of the fractal.
    # A higher 'recursion_level' will result in more detail and
    # potentially a longer generation time.
    recursion_level = 6

    # Call the function to create and save the fractal image.
    create_fractal_image(image_width, image_height, recursion_level)

    # You can experiment by changing 'recursion_level' to see how the fractal changes.
    # For example, try recursion_level = 8 or recursion_level = 4.
    # Also, try changing image_width and image_height.