import sys
import time
from contextlib import contextmanager

# Learning Objective:
# This tutorial demonstrates how to build a reusable command-line progress tracker
# using Python's generators and context managers.
# You will learn:
# 1. How generators (`yield`) can lazily produce values and inject side effects (like printing progress).
# 2. How context managers (`with` statement, `@contextlib.contextmanager`) provide clean setup and teardown logic.
# 3. Techniques for dynamic console output (`\r`, `sys.stdout.flush()`).
# 4. How to combine these powerful features to create practical utilities.
# This utility is immediately useful for monitoring long-running loops in your scripts.


# --- Part 1: The Core Progress Display Logic (Generator) ---
# This is an internal utility function that wraps an iterable.
# For each item it yields, it also updates a dynamic progress bar on the console.
def _progress_generator_impl(iterable, total_items, prefix='', bar_length=40):
    """
    Internal generator implementation for progress tracking.
    It yields items from the original iterable while updating a progress bar
    on the console line.

    Args:
        iterable: The original iterable whose items will be yielded.
        total_items: The total number of items to process, required for percentage calculation.
        prefix: A string displayed before the progress bar (e.g., "Processing:").
        bar_length: The fixed width of the progress bar in characters.
    """
    # We use `enumerate(iterable, 1)` to get both the index (starting from 1)
    # and the item from the iterable. This is intuitive for displaying "item 1 of N".
    for current_count, item in enumerate(iterable, 1):
        # Calculate progress percentage.
        # We cast to float to ensure floating-point division for accurate percentages.
        percent = (current_count / total_items) * 100

        # Calculate how much of the bar should be "filled".
        # This converts the percentage into a segment of `bar_length`.
        filled_length = int(bar_length * current_count / total_items)

        # Construct the visual progress bar string.
        # The filled part uses '#', and the empty part uses '-'.
        bar = '#' * filled_length + '-' * (bar_length - filled_length)

        # Construct the full progress string to display.
        # `\r` (carriage return) is key here: it moves the cursor to the beginning
        # of the current line, allowing us to overwrite the previously printed progress.
        progress_str = (
            f"\r{prefix} |{bar}| {percent:.1f}% ({current_count}/{total_items})"
        )

        # Write the string to standard output.
        # `end=''` prevents Python from automatically adding a newline character.
        # This is essential for keeping the progress bar on a single line and overwriting it.
        sys.stdout.write(progress_str)

        # `sys.stdout.flush()` forces the output buffer to be written to the console immediately.
        # Without this, output might be buffered and only appear after some delay,
        # making the progress bar appear to jump instead of update smoothly.
        sys.stdout.flush()

        # The core of a generator: `yield` returns the current item to the caller.
        # Execution of this function pauses here until the next item is requested
        # (e.g., by the next iteration of a `for` loop).
        yield item

    # After the loop finishes (all items have been yielded), we print a final newline.
    # This is crucial so that any subsequent `print()` statements appear on a new line,
    # below the completed progress bar, instead of overwriting it or appearing on the same line.
    sys.stdout.write('\n')
    sys.stdout.flush() # Ensure this final newline is also immediately visible.


# --- Part 2: The Context Manager (User Interface) ---
# This provides a clean 'with' statement interface for our progress tracker.
# It handles determining the total, setting up the generator, and ensuring final output.
@contextmanager
def track_progress(iterable, total=None, prefix='Progress:', bar_length=40):
    """
    A context manager that provides a progress-tracking iterable.
    It automatically calculates the total number of items if the iterable
    supports `len()`, otherwise, `total` must be provided explicitly.

    Usage:
        with track_progress(my_list, prefix="Processing items:") as tracked_items:
            for item in tracked_items:
                # process item
    """
    # Explanation of `@contextlib.contextmanager`:
    # This decorator transforms a simple generator function (like `track_progress` itself)
    # into a context manager that can be used with `with` statements.
    # - Code *before* the `yield` statement acts as the `__enter__` method (setup phase).
    # - Code *after* the `yield` statement acts as the `__exit__` method (teardown phase).
    # - The value passed to the `yield` statement becomes the value assigned to the `as` variable
    #   in the `with` statement (e.g., `tracked_items` in the example above).

    # First, determine the total number of items if not explicitly provided.
    # This is essential for calculating accurate percentages for the progress bar.
    if total is None:
        try:
            # Attempt to get the length if the iterable supports it (e.g., list, tuple, string).
            total = len(iterable)
        except TypeError:
            # If `len()` fails (e.g., for a generator or custom iterator without `__len__`),
            # we cannot determine the total. We'll print a warning and yield the original iterable
            # without progress tracking so the program can still run.
            print(
                "Warning: Iterable has no `len()` method. Please provide `total` explicitly "
                "for accurate progress tracking (e.g., `track_progress(my_gen(), total=100)`).",
                file=sys.stderr
            )
            # Yield the original iterable directly, without tracking, so the program can still run.
            yield iterable
            return # Exit the context manager's function early.

    # If `total` is successfully determined (or was provided), we create our progress generator.
    # This is the actual iterable that the user will loop over.
    progress_iterable = _progress_generator_impl(iterable, total, prefix, bar_length)

    # The `yield` here is the core of the context manager's `__enter__` behavior.
    # The value `progress_iterable` is passed to the `as` variable of the `with` statement.
    # Execution of the context manager pauses here, and the code inside the `with` block runs.
    yield progress_iterable

    # Execution resumes here AFTER the `with` block finishes (either normally or due to an error).
    # In this specific tracker, the `_progress_generator_impl` already handles printing a final newline
    # after its loop completes, so there's not much explicit teardown needed here for display purposes.
    # However, this is where you'd typically add other cleanup or finalization code if necessary.
    pass


# --- Example Usage ---
# This section demonstrates how to use the `track_progress` context manager
# to monitor various long-running tasks.

def simulate_task(item, delay_seconds=0.05):
    """
    A simple helper function to simulate a long-running operation for an item.
    Pauses execution for a given duration.
    """
    time.sleep(delay_seconds) # Pause execution to simulate work.
    return item # In a real scenario, this would return processed data.


if __name__ == "__main__":
    print("--- Example 1: Tracking a list of numbers ---")
    my_items = list(range(1, 21)) # A list of 20 numbers.

    # Use the context manager to wrap the iterable (`my_items`).
    # The `with` statement ensures proper setup (preparing the generator) and
    # teardown (printing the final newline).
    # `tracked_numbers` will be the generator from the context manager that yields items
    # while updating the progress bar.
    processed_results = []
    with track_progress(my_items, prefix="Processing numbers:") as tracked_numbers:
        for num in tracked_numbers:
            # Inside this loop, `num` is yielded by our progress generator.
            # The progress bar is updated automatically each time `num` is yielded.
            result = simulate_task(num, 0.1) # Simulate a longer task for each number.
            processed_results.append(result)

    print("Processing complete! (Results not displayed to keep output clean)")
    # print(f"Results: {processed_results[:5]}...") # Uncomment to display first few results.
    print("-" * 60)


    print("--- Example 2: Tracking a different task with custom bar length ---")
    task_names = ["Download A", "Process B", "Upload C", "Analyze D", "Clean E", "Report F"]

    # You can customize the prefix and bar length for better visual fit.
    # For lists and other sequence types, the 'total' argument is automatically inferred using `len()`.
    with track_progress(task_names, prefix="Executing tasks:", bar_length=60) as tracked_tasks:
        for task in tracked_tasks:
            # We can also print other information, but need to be careful with `\r`.
            # Printing a full line with `\r` and flushing *before* the progress bar updates
            # helps avoid flickering or conflicts. `ljust` pads the string.
            sys.stdout.write(f"\r  Currently working on: {task}".ljust(80))
            sys.stdout.flush()
            simulate_task(task, 0.2) # Simulate work for each task.

    print("All tasks finished!")
    print("-" * 60)


    print("--- Example 3: Explicitly providing total for an unknown length iterable ---")
    # Imagine `read_large_file_lines` is a generator that yields lines one by one.
    # A generator function itself doesn't have a `len()`.
    def read_large_file_lines(num_lines_to_generate):
        for i in range(1, num_lines_to_generate + 1):
            # In a real scenario, this would read from a file.
            yield f"Line {i} content from file simulation"

    total_lines = 100
    # Here, we MUST provide 'total' because `read_large_file_lines(total_lines)` returns a generator,
    # which doesn't have a `len()`.
    with track_progress(read_large_file_lines(total_lines), total=total_lines, prefix="Reading file:") as lines:
        for line in lines:
            simulate_task(line, 0.02) # Process each line quickly.

    print("File reading complete!")
    print("-" * 60)

    print("--- Example 4: What happens if total is not provided for an unknown length iterable? ---")
    # This demonstrates the warning message from our context manager.
    def infinite_generator():
        count = 0
        while True:
            count += 1
            yield f"Infinite item {count}"

    # We'll just take the first 5 items to show the warning and then stop.
    # The progress tracker won't show a percentage or bar because 'total' is unknown,
    # and will simply yield the original items.
    print("Expecting a warning message below:")
    with track_progress(infinite_generator(), prefix="Processing unknown length:") as unknown_items:
        # We manually limit the loop here. If you removed `for _ in range(5):` and `next()`,
        # this would run infinitely because the generator itself is infinite and the tracker
        # cannot stop it (it just wraps it).
        for _ in range(5):
            item = next(unknown_items) # Manually get the next item from the wrapped generator.
            sys.stdout.write(f"\r  Processing: {item}".ljust(80))
            sys.stdout.flush()
            simulate_task(item, 0.3)
    print("\nFinished processing a few items from unknown length iterable (see warning above).")
    print("-" * 60)