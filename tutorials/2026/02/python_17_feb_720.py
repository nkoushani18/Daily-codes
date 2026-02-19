# Heap Operations in Python
=====================================

This script teaches you about heap operations using Python's built-in `heapq` module. The `heapq` module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

## Importing the heapq Module
--------------------------------

First, we need to import the `heapq` module.
```python
import heapq
```

## Creating a Heap
--------------------

A heap is a special type of binary tree where each parent node is either greater than (in a max heap) or less than (in a min heap) its children. We can create a heap using the `heapify()` function from the `heapq` module.
```python
# Create a list to serve as our heap
numbers = [12, 3, 56, 2, 8]

# Convert the list into a heap
heapq.heapify(numbers)
print("Heap:", numbers)
```

## Heap Operations
-------------------

### Heappush()
--------------

The `heappush()` function adds an element to the heap. The new element will be inserted in its correct position based on the heap property.
```python
# Add some elements to the heap
heapq.heappush(numbers, 10)
heapq.heappush(numbers, -5)

print("Heap after push:", numbers)
```

### Heappop()
-------------

The `heappop()` function removes and returns the smallest element from the heap. If the heap is empty, it raises an `IndexError`.
```python
# Remove and return the smallest element from the heap
smallest_element = heapq.heappop(numbers)

print("Smallest Element:", smallest_element)
```

### Heapify()
-------------

The `heapify()` function converts a list into a heap. This operation is done in O(n) time.
```python
# Convert a list into a heap
numbers = [12, 3, 56, 2, 8]
heapq.heapify(numbers)
print("Heap:", numbers)
```

## Example Usage and Test
---------------------------

Here's an example usage of the `heapq` module: