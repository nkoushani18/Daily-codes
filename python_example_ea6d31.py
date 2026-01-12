# Visualize Real-time Sensor Data with Matplotlib and a Simple Data Generation Loop

# Learning Objective:
# This tutorial demonstrates how to visualize continuously updating sensor data
# in a real-time manner using Python. We will simulate sensor readings by
# generating data in a loop and then plot this data using Matplotlib's
# animation capabilities. This is a foundational skill for many applications,
# including monitoring scientific experiments, visualizing system performance,
# or creating interactive dashboards.

# Key Concepts Covered:
# 1. Simulating real-time data generation.
# 2. Using Matplotlib for plotting.
# 3. Employing Matplotlib's animation module for dynamic updates.
# 4. Managing data buffer to display a history of readings.

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import random

# --- Configuration ---
# Define the maximum number of data points to display on the plot at any given time.
# This creates a "scrolling" effect, showing the most recent data.
MAX_DATA_POINTS = 100

# Define the interval between plot updates in milliseconds.
# A smaller interval means faster updates, but can consume more CPU.
UPDATE_INTERVAL_MS = 50

# --- Data Storage ---
# These lists will store our simulated sensor readings over time.
# We'll use them to keep track of the history of our data.
# 'x_data' will store the time points (or sequential indices).
# 'y_data' will store the actual sensor readings.
x_data = []
y_data = []

# --- Initialization ---
# This function sets up the initial state of our plot.
# It's called once at the beginning of the animation.
def init():
    # Set the limits for the x-axis. We start with an empty range.
    ax.set_xlim(0, MAX_DATA_POINTS)
    # Set the limits for the y-axis. We'll adjust this dynamically later
    # as we get more data to ensure all points are visible.
    ax.set_ylim(0, 100) # Initial guess, will auto-adjust

    # Return the plot elements that will be updated.
    # In this case, it's the line object that we'll be drawing on.
    return line,

# --- Data Generation and Update Function ---
# This function is called repeatedly by the animation framework.
# It simulates reading a sensor, updates our data lists, and redraws the plot.
def update(frame):
    # Simulate reading a sensor value.
    # For this example, we're using a random number between 0 and 100.
    # In a real-world scenario, you would replace this with actual sensor readings
    # from a device (e.g., Arduino, Raspberry Pi, or a network API).
    current_sensor_reading = random.randint(0, 100)

    # Get the current number of data points already plotted.
    num_points = len(x_data)

    # --- Data Management (Buffer) ---
    # We want to display only the last MAX_DATA_POINTS.
    # If we have more points than allowed, remove the oldest one.
    if num_points >= MAX_DATA_POINTS:
        # Remove the first element (oldest data) from both lists.
        x_data.pop(0)
        y_data.pop(0)
        # After removing the oldest, we'll add the new one.

    # --- Append New Data ---
    # Add the new sensor reading to our data lists.
    # For 'x_data', we use the current number of points as a simple time index.
    # This creates a sequence like 0, 1, 2, ... which is useful for plotting.
    x_data.append(num_points)
    y_data.append(current_sensor_reading)

    # --- Plot Update ---
    # Update the data for our line plot.
    line.set_data(x_data, y_data)

    # --- Axis Auto-scaling ---
    # Adjust the x-axis limits to match the current data range.
    # We set the left limit to be the current number of points minus MAX_DATA_POINTS,
    # ensuring we always see the last MAX_DATA_POINTS if available.
    # If we have fewer than MAX_DATA_POINTS, the left limit will be 0.
    ax.set_xlim(max(0, num_points - MAX_DATA_POINTS), num_points)

    # Adjust the y-axis limits to ensure all data points are visible.
    # We find the minimum and maximum values in our current y_data and set the
    # y-axis limits slightly larger to provide some padding.
    if y_data: # Only update if there's data to avoid errors on empty lists
        min_y = min(y_data)
        max_y = max(y_data)
        # Add a small buffer for better visualization
        buffer = (max_y - min_y) * 0.1
        ax.set_ylim(max(0, min_y - buffer), max_y + buffer)
    else:
        # If no data, reset to a default range to avoid issues.
        ax.set_ylim(0, 100)

    # Return the plot elements that have been modified.
    # This tells the animation framework which parts of the plot need to be redrawn.
    return line,

# --- Main Execution ---
if __name__ == "__main__":
    # 1. Create a figure and an axes object.
    # A figure is the overall window or page, and axes is the actual plotting area.
    fig, ax = plt.subplots()

    # 2. Create an initial empty line object.
    # We'll update this line's data in the 'update' function.
    # 'animated=True' is important for efficient animation.
    line, = ax.plot([], [], lw=2, animated=True) # lw is line width

    # 3. Set plot labels for clarity.
    ax.set_xlabel("Time (sample)")
    ax.set_ylabel("Sensor Value")
    ax.set_title("Real-time Sensor Data Visualization")

    # 4. Create the animation object.
    # 'ani' is our animation instance.
    # 'fig' is the figure to animate.
    # 'update' is the function that will be called for each frame.
    # 'init_func' is the function to call once at the beginning.
    # 'frames' can be set to None for a continuous loop.
    # 'interval' is the delay between frames in milliseconds.
    # 'blit=True' is an optimization that only redraws the parts that have changed.
    ani = animation.FuncAnimation(fig,
                                  update,
                                  init_func=init,
                                  frames=None, # Loop indefinitely
                                  interval=UPDATE_INTERVAL_MS,
                                  blit=True,
                                  cache_frame_data=False) # Prevent caching if data is truly live

    # 5. Display the plot.
    # 'plt.show()' starts the Matplotlib event loop, which is necessary for
    # animations to run and for interactive features to work.
    plt.show()

# --- Example Usage ---
# To run this code:
# 1. Save it as a Python file (e.g., real_time_plot.py).
# 2. Make sure you have Matplotlib and NumPy installed:
#    pip install matplotlib numpy
# 3. Run the file from your terminal:
#    python real_time_plot.py
#
# You will see a plot window appear, and the line on the plot will move
# and update dynamically, simulating real-time sensor data.