# Interval Scheduling using Greedy Algorithm
import sys

def is_sorted(lst):
    """Check if the list of intervals is sorted by their end times"""
    return all(lst[i][1] <= lst[i+1][1] for i in range(len(lst)-1))

def greedy_interval_scheduling(intervals):
    """
    Greedily select the longest interval that does not conflict with previously selected intervals
    """
    if not intervals:
        return []

    # Sort the intervals by their end times
    intervals.sort(key=lambda x: x[1])

    result = [intervals[0]]
    for i in range(1, len(intervals)):
        # If the current interval does not conflict with the previously selected intervals,
        # add it to the result list
        if intervals[i][0] >= result[-1][1]:
            result.append(intervals[i])

    return result

def print_intervals(intervals):
    """Print the selected intervals in a readable format"""
    for i, interval in enumerate(intervals):
        print(f"Interval {i+1}: ({interval[0]}, {interval[1]})")

# Example usage
intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
selected_intervals = greedy_interval_scheduling(intervals)
print("Selected Intervals:")
print_intervals(selected_intervals)