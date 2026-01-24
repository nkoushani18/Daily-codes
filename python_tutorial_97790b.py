# Learning Objective:
# This tutorial will guide you through building a simple, interactive data visualization tool
# using Python's Plotly library. We will focus on creating a scatter plot that allows users
# to dynamically change the color of data points based on a selected column from their dataset.
# This demonstrates a fundamental concept in interactive visualization: user-driven data exploration.

# Import necessary libraries
# We need pandas for data manipulation and plotly.express for creating interactive plots easily.
import pandas as pd
import plotly.express as px

# --- Step 1: Load and Prepare Your Data ---
# For this tutorial, we'll create a sample DataFrame. In a real-world scenario,
# you would load your data from a CSV, Excel file, or database using pandas.
# Creating a DataFrame with diverse data types to showcase color mapping.
data = {
    'X_Axis': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y_Axis': [5, 6, 4, 7, 3, 8, 2, 9, 1, 10],
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Value': [100, 150, 120, 180, 110, 200, 130, 160, 140, 190]
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame to understand its structure.
# This helps in identifying which columns can be used for plotting.
print("--- Sample DataFrame ---")
print(df.head())
print("\n")

# --- Step 2: Create the Interactive Scatter Plot ---
# Plotly Express (px) is a high-level interface for Plotly, making it easy
# to create common plot types with minimal code.

# We are creating a scatter plot.
# 'df' is our pandas DataFrame.
# 'x' specifies the column for the x-axis.
# 'y' specifies the column for the y-axis.
# 'color' is the key to interactivity! When a user selects a column here,
# Plotly will color the points based on the values in that column.
# 'hover_data' allows us to display additional information when hovering over a point.
# 'title' provides a descriptive title for our visualization.
fig = px.scatter(df,
                 x="X_Axis",
                 y="Y_Axis",
                 color="Category",  # Initially coloring by 'Category'
                 hover_data=['Value'], # Display 'Value' on hover
                 title="Interactive Scatter Plot: Explore Data by Category")

# --- Step 3: Enhance Interactivity (Optional but Recommended) ---
# Plotly figures have a 'update_layout' method to customize the appearance
# and interactive features. Here, we're enabling a more interactive feel.

fig.update_layout(
    # The legend in Plotly is interactive by default, allowing users to click
    # on legend items to hide/show corresponding data points.
    # This layout update is more about general plot aesthetics and might not
    # be strictly necessary for basic interactivity but good to know.
    # For this specific example, the primary interactivity comes from the 'color' argument.
    # You could add more complex controls with Dash, but for Plotly Express,
    # the 'color' parameter is the main driver for dynamic coloring.
)

# --- Step 4: Display the Visualization ---
# The 'fig.show()' method renders the interactive plot.
# This will typically open the plot in your default web browser or
# display it inline if you are using an environment like Jupyter Notebook.
print("--- Displaying Interactive Plot ---")
print("The plot should open in your browser or display inline.")
fig.show()

# --- Example Usage and Further Exploration ---
# To explore the data visually by a different column (e.g., 'Value'),
# you would simply re-run the 'px.scatter' function with a different 'color' argument.
# For instance, to color by 'Value':
# fig_by_value = px.scatter(df,
#                           x="X_Axis",
#                           y="Y_Axis",
#                           color="Value", # Color by the numerical 'Value' column
#                           hover_data=['Category'],
#                           title="Interactive Scatter Plot: Explore Data by Value")
# fig_by_value.show()
# This demonstrates how easily you can pivot your visualization based on different
# data attributes directly within Plotly Express.