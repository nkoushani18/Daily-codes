# Learning Objective:
# This tutorial will teach you how to programmatically generate and visualize
# colorful fractal patterns in Python. We will focus on the Mandelbrot set,
# a classic example of a fractal, and explore how to map its properties
# to colors for a visually appealing result.

# Import necessary libraries
# We'll use NumPy for efficient numerical operations, especially array manipulation.
# Matplotlib is for plotting and visualizing our fractal.
import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iterations):
    """
    Generates the Mandelbrot set for a given region and resolution.

    Args:
        width (int): The width of the output image in pixels.
        height (int): The height of the output image in pixels.
        x_min (float): The minimum real value for the complex plane.
        x_max (float): The maximum real value for the complex plane.
        y_min (float): The minimum imaginary value for the complex plane.
        y_max (float): The maximum imaginary value for the complex plane.
        max_iterations (int): The maximum number of iterations to perform for each point.

    Returns:
        numpy.ndarray: A 2D array where each element represents the number of
                       iterations it took for the corresponding point to escape
                       the Mandelbrot set. If a point never escapes, it's assigned
                       max_iterations.
    """
    # Create a grid of complex numbers corresponding to each pixel.
    # `np.linspace` creates evenly spaced numbers over a specified interval.
    # `np.meshgrid` creates coordinate matrices from coordinate vectors.
    # This efficiently generates all (x, y) coordinates for our complex plane.
    x, y = np.meshgrid(np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height))

    # `c` represents the complex number for each pixel (real part x, imaginary part y).
    c = x + 1j * y

    # `z` is initialized to zero for all points. This is the starting point
    # for the iteration `z = z^2 + c`.
    z = np.zeros_like(c)

    # `iterations` array will store the escape count for each pixel.
    # Initialize it with zeros.
    iterations = np.zeros(c.shape, dtype=int)

    # The core Mandelbrot iteration.
    # We iterate `max_iterations` times, updating `z` according to the formula.
    # `np.abs(z)` calculates the magnitude of the complex number `z`.
    # If the magnitude of `z` exceeds 2, it means the point will diverge
    # to infinity and is NOT part of the Mandelbrot set.
    # The condition `np.abs(z) <= 2` checks for points that are *still*
    # potentially within the set. We only update these points.
    for i in range(max_iterations):
        # Find the points that have not yet escaped (magnitude <= 2).
        # We use a boolean mask to select these points.
        not_escaped_mask = np.abs(z) <= 2

        # Only update `z` and `iterations` for points that haven't escaped.
        # This is crucial for efficiency.
        z[not_escaped_mask] = z[not_escaped_mask]**2 + c[not_escaped_mask]
        iterations[not_escaped_mask] += 1

    # For points that reached max_iterations without escaping, we assign max_iterations.
    # This signifies they are considered part of the Mandelbrot set.
    # For points that escaped, their iteration count (how many steps to escape)
    # is already recorded.
    return iterations

def visualize_fractal(iterations, cmap='hot'):
    """
    Visualizes the Mandelbrot set iterations using a colormap.

    Args:
        iterations (numpy.ndarray): The 2D array of iteration counts from
                                    `generate_mandelbrot_set`.
        cmap (str): The colormap to use for visualization (e.g., 'hot', 'viridis', 'plasma').
    """
    # Create a figure and an axes object for plotting.
    fig, ax = plt.subplots(figsize=(10, 10))

    # Display the iteration counts as an image.
    # `interpolation='nearest'` ensures sharp pixels, preventing blurring.
    # `cmap` applies a color mapping to the iteration values.
    # Darker colors typically represent points that escaped quickly (far from the set),
    # while brighter colors represent points that took longer to escape or are within the set.
    im = ax.imshow(iterations, cmap=cmap, extent=[-2, 1, -1.5, 1.5], interpolation='nearest')

    # Add a colorbar to show the mapping between colors and iteration counts.
    # This helps in understanding which colors correspond to how many iterations.
    plt.colorbar(im, label='Iterations to Escape')

    # Set the title of the plot.
    ax.set_title('Mandelbrot Set Fractal')
    ax.set_xlabel('Real Part')
    ax.set_ylabel('Imaginary Part')

    # Show the plot.
    plt.show()

# --- Example Usage ---
if __name__ == "__main__":
    # Define parameters for the Mandelbrot set generation.
    # These determine the region of the complex plane we're exploring
    # and the level of detail.
    image_width = 800
    image_height = 800
    real_min = -2.0
    real_max = 1.0
    imaginary_min = -1.5
    imaginary_max = 1.5
    max_iterations_value = 100  # Higher values mean more detail but slower computation.

    # Generate the Mandelbrot set data.
    print("Generating Mandelbrot set...")
    mandelbrot_data = generate_mandelbrot_set(
        image_width,
        image_height,
        real_min,
        real_max,
        imaginary_min,
        imaginary_max,
        max_iterations_value
    )
    print("Generation complete. Visualizing...")

    # Visualize the generated fractal.
    # You can experiment with different colormaps like 'viridis', 'plasma', 'inferno', 'cividis'.
    visualize_fractal(mandelbrot_data, cmap='viridis')

    # Example of zooming into a specific region (the "seahorse valley").
    print("Generating zoomed-in view...")
    zoom_real_min = -0.74877
    zoom_real_max = -0.74872
    zoom_imaginary_min = 0.12364
    zoom_imaginary_max = 0.12369
    zoom_iterations = 500 # Increased iterations for finer detail in zoomed view.

    zoomed_mandelbrot_data = generate_mandelbrot_set(
        image_width,
        image_height,
        zoom_real_min,
        zoom_real_max,
        zoom_imaginary_min,
        zoom_imaginary_max,
        zoom_iterations
    )
    print("Zoomed view generation complete. Visualizing...")
    visualize_fractal(zoomed_mandelbrot_data, cmap='inferno')