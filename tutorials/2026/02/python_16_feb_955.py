import heapq

# Heap operations: this file teaches you how to use Python's built-in heap data structure to efficiently insert and retrieve the smallest/ largest element from a collection of elements.

class MinHeap:
    def __init__(self):
        # Initialize an empty list to store our heap elements
        self.heap = []

    def parent(self, i):
        # Calculate the index of the parent node at position 'i'
        return (i - 1) // 2

    def left_child(self, i):
        # Calculate the index of the left child node at position 'i'
        return 2 * i + 1

    def right_child(self, i):
        # Calculate the index of the right child node at position 'i'
        return 2 * i + 2

    def swap(self, i, j):
        # Swap elements at positions 'i' and 'j'
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        # Insert a new element into the heap
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            parent = self.parent(i)
            if self.heap[parent] <= self.heap[i]:
                break
            self.swap(parent, i)
            i = parent

    def extract_min(self):
        # Remove and return the smallest element from the heap
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        i = 0

        while True:
            left = self.left_child(i)
            right = self.right_child(i)

            smallest = i
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break
            self.swap(smallest, i)
            i = smallest

        return min_val

# Example usage/test
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)

while True:
    print("1. Extract minimum")
    print("2. Print heap size")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Minimum element:", min_heap.extract_min())
    elif choice == "2":
        print("Heap size:", len(min_heap.heap))
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")