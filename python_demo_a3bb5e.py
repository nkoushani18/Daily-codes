# Learning Objective:
# This tutorial will teach you how to create a simple, interactive GUI application
# using Python's Tkinter library to visualize your personal spending habits.
# We will focus on basic GUI elements, event handling, and simple data visualization.

# Import the Tkinter library, which is Python's standard GUI toolkit.
import tkinter as tk
# We'll use the ttk module for themed widgets, which generally look better.
from tkinter import ttk
# For this example, we'll use a simple list to store spending data.
# In a real application, you'd likely use a database or file.
from collections import defaultdict # defaultdict simplifies counting items

# Define a function to create and manage our spending visualization application.
def create_spending_visualizer():
    # --- Setting up the Main Window ---

    # Create the main application window. This is the container for all other widgets.
    root = tk.Tk()
    # Set the title that appears in the window's title bar.
    root.title("Personal Spending Visualizer")

    # --- Data Storage ---

    # A dictionary to store spending by category.
    # defaultdict(int) automatically initializes a new key with a value of 0 if it doesn't exist.
    # This avoids needing to check if a category is already in the dictionary.
    spending_data = defaultdict(int)

    # --- GUI Elements (Widgets) ---

    # Create a Label widget to instruct the user.
    instruction_label = ttk.Label(root, text="Enter Expense:")
    # Place the label in the window using the 'grid' layout manager.
    # 'row' and 'column' specify its position. 'pady' adds vertical padding.
    instruction_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # Create an Entry widget for the user to type in expense details.
    # This is where the user will input amounts and categories.
    expense_entry = ttk.Entry(root, width=30)
    # Place the entry widget next to the label.
    expense_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew") # sticky="ew" makes it stretch horizontally

    # Create a Label widget for the category input.
    category_label = ttk.Label(root, text="Category:")
    category_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    # Create an Entry widget for the category.
    category_entry = ttk.Entry(root, width=30)
    category_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    # Create a Label widget to display current spending summary.
    summary_label = ttk.Label(root, text="Spending Summary:", font=("Arial", 12, "bold"))
    summary_label.grid(row=3, column=0, columnspan=2, padx=5, pady=10) # columnspan makes it span two columns

    # Create a Text widget to display the spending summary.
    # Text widgets allow for multi-line text display and are good for lists.
    # We set a height and width for better initial appearance.
    summary_text = tk.Text(root, height=10, width=40, wrap=tk.WORD) # wrap=tk.WORD prevents words from being cut
    summary_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    # Initially, disable the Text widget so the user can't directly edit it.
    summary_text.config(state=tk.DISABLED)

    # --- Event Handling Functions ---

    # This function is called when the "Add Expense" button is clicked.
    def add_expense():
        # Get the text from the expense and category entry fields.
        expense_str = expense_entry.get()
        category = category_entry.get().strip() # .strip() removes leading/trailing whitespace

        # Input validation: Ensure category is not empty and expense is a valid number.
        if not category:
            update_summary("Error: Category cannot be empty.")
            return
        try:
            # Convert the expense string to a float (decimal number).
            expense_amount = float(expense_str)
            if expense_amount < 0:
                update_summary("Error: Expense amount cannot be negative.")
                return
        except ValueError:
            # If conversion fails (e.g., user typed text), show an error.
            update_summary("Error: Invalid expense amount. Please enter a number.")
            return

        # Add the valid expense amount to the corresponding category in our data.
        spending_data[category] += expense_amount

        # Clear the entry fields after successful addition.
        expense_entry.delete(0, tk.END) # Delete from the beginning (0) to the end (tk.END)
        category_entry.delete(0, tk.END)

        # Refresh the summary display to show the updated spending.
        update_summary()

    # This function updates the spending summary display.
    def update_summary(error_message=None):
        # Enable the Text widget temporarily to modify its content.
        summary_text.config(state=tk.NORMAL)
        # Clear any existing content in the Text widget.
        summary_text.delete(1.0, tk.END) # Delete from line 1, character 0 to the end.

        if error_message:
            summary_text.insert(tk.END, error_message)
        else:
            # If there's no error, iterate through the spending data.
            total_spending = 0
            # Sort categories alphabetically for a consistent display.
            for category in sorted(spending_data.keys()):
                amount = spending_data[category]
                # Format the string to display category and amount.
                summary_text.insert(tk.END, f"{category}: ${amount:.2f}\n") # :.2f formats to 2 decimal places
                total_spending += amount
            # Add a line for the total spending.
            summary_text.insert(tk.END, "--------------------\n")
            summary_text.insert(tk.END, f"Total: ${total_spending:.2f}\n")

        # Disable the Text widget again after updating.
        summary_text.config(state=tk.DISABLED)

    # --- Buttons ---

    # Create a Button widget to trigger adding an expense.
    # 'command' links the button click event to our add_expense function.
    add_button = ttk.Button(root, text="Add Expense", command=add_expense)
    # Place the button below the entry fields.
    add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    # --- Running the Application ---

    # Start the Tkinter event loop. This makes the window appear and
    # listen for user interactions (like button clicks, typing).
    root.mainloop()

# --- Example Usage ---

# This block checks if the script is being run directly (not imported as a module).
if __name__ == "__main__":
    # Call the function to create and run our spending visualizer.
    create_spending_visualizer()

# How to use this program:
# 1. Run the Python script.
# 2. A window will appear with input fields for "Expense" and "Category".
# 3. Enter a numerical amount in the "Expense" field (e.g., 25.50).
# 4. Enter a category for that expense in the "Category" field (e.g., Groceries).
# 5. Click the "Add Expense" button.
# 6. The expense will be added to the summary list.
# 7. You can add more expenses, and the summary will update.
# 8. The summary will show each category and its total spending, as well as the overall total.
# 9. If you enter invalid input (e.g., text for expense, empty category), an error message will appear.