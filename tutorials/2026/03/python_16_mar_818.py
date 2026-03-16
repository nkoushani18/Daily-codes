# Heap Operations in Python

class MinHeap:
    def __init__(self):
        # Initialize an empty list to store the heap elements
        self.heap = []

    def parent(self, i):
        # Calculate the index of the parent node
        return (i - 1) // 2

    def left_child(self, i):
        # Calculate the index of the left child node
        return 2 * i + 1

    def right_child(self, i):
        # Calculate the index of the right child node
        return 2 * i + 2

    def insert(self, value):
        # Add a new element to the heap by inserting it at the end and then bubbbling up
        self.heap.append(value)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap the current node with its parent if it is smaller
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            # Move up to the parent node
            i = self.parent(i)

    def delete_min(self):
        # Delete and return the minimum element from the heap by replacing it with the last element and then bubbled down
        if len(self.heap) == 0:
            raise ValueError("Heap is empty")
        min_value = self.heap[0]
        # Replace the root node with the last element in the heap
        self.heap[0] = self.heap.pop()
        i = 0
        while True:
            left_child_index = self.left_child(i)
            right_child_index = self.right_child(i)
            smallest = i
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index
            # If the smallest element is not the current node, swap them and move up
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def print_heap(self):
        # Print the heap elements
        for i in range(len(self.heap)):
            print(f"Index {i}: {self.heap[i]}")

# Example usage
if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(2)
    min_heap.insert(8)
    min_heap.insert(1)
    min_heap.insert(3)

    print("Initial heap:")
    min_heap.print_heap()

    min_heap.delete_min()
    print("\nAfter deleting the minimum element:")
    min_heap.print_heap()

    min_heap.delete_min()
    print("\nAfter deleting the second minimum element:")
    min_heap.print_heap()