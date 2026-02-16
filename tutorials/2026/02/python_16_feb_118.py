import heapq

def findIntervals(intervals):
    # Sort the intervals by their end time
    intervals.sort(key=lambda x: x[1])

    # Initialize a min heap with the first interval
    min_heap = [intervals[0]]
    prev_end = intervals[0][1]

    # Iterate through the sorted intervals
    for i in range(1, len(intervals)):
        if intervals[i][0] >= prev_end:
            heapq.heappush(min_heap, intervals[i])
            prev_end = intervals[i][1]

    return min_heap

# Test the function
intervals = [(2, 4), (3, 5), (6, 8)]
print(findIntervals(intervals))