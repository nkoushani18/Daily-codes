import random

def greedy_interval_scheduling(intervals):
    # Sort the intervals by their end times
    intervals.sort(key=lambda x: x[1])

    # Initialize the end time of the last scheduled interval
    last_end_time = -1

    # Initialize the list of scheduled intervals
    scheduled_intervals = []

    # Iterate over the sorted intervals
    for interval in intervals:
        # If the start time of the current interval is greater than or equal to the end time of the last scheduled interval
        if interval[0] >= last_end_time:
            # Add the current interval to the list of scheduled intervals
            scheduled_intervals.append(interval)
            # Update the end time of the last scheduled interval
            last_end_time = interval[1]
        else:
            # If the start time of the current interval is less than the end time of the last scheduled interval
            # and the end time of the current interval is greater than the end time of the last scheduled interval
            if interval[1] > last_end_time:
                # Add the current interval to the list of scheduled intervals
                scheduled_intervals.append(interval)
                # Update the end time of the last scheduled interval
                last_end_time = interval[1]

    # Return the list of scheduled intervals
    return scheduled_intervals

# Generate a list of random intervals
intervals = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(5)]

# Sort the intervals by their end times
intervals.sort(key=lambda x: x[1])

# Print the original intervals
print("Original Intervals:")
for interval in intervals:
    print(interval)

# Print the scheduled intervals
scheduled_intervals = greedy_interval_scheduling(intervals)
print("\nScheduled Intervals:")
for interval in scheduled_intervals:
    print(interval)

# Print the total time of the scheduled intervals
total_time = sum(interval[1] for interval in scheduled_intervals)
print("\nTotal Time of Scheduled Intervals:", total_time)