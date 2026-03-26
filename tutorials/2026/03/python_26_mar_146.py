# Heap Operations in Python

import heapq

def create_heap(data):
    """
    Creates a min heap from the given data.

    :param data: list of elements to be heapified.
    :return: a min heap represented as a heap data structure.
    """
    # Convert the list into a heap using heapq.heapify()
    heapq.heapify(data)
    return data

def print_heap(heap):
    """
    Prints the elements in the given heap.

    :param heap: a min heap to be printed.
    """
    # Use heapq.heappop() and heapq.heappush() to extract and insert elements
    while heap:
        print("Heap:", heap)
        element = heapq.heappop(heap)  # Extract the smallest element
        print("Popped Element:", element)
        if heap:
            heapq.heappush(heap, element)  # Insert the extracted element back into the heap

def heap_insert(data, new_element):
    """
    Inserts a new element into the given min heap.

    :param data: a min heap.
    :param new_element: the element to be inserted.
    """
    # Use heapq.heappush() to insert the new element
    heapq.heappush(data, new_element)

def heap_extract_min(heap):
    """
    Extracts and returns the smallest element from the given min heap.

    :param heap: a min heap.
    :return: the smallest element in the heap.
    """
    # Use heapq.heappop() to extract the smallest element
    return heapq.heappop(heap)

def main():
    # Create a list of elements to be heapified
    data = [4, 2, 9, 6, 5, 1]
    
    print("Original List:", data)
    create_heap(data)  # Convert the list into a min heap
    
    # Insert new elements into the heap
    heap_insert(data, 8)
    heap_insert(data, 3)
    print("Heap after insertions:", data)
    
    # Extract and print the smallest element from the heap
    extracted_element = heap_extract_min(data)
    print("Smallest Element:", extracted_element)

if __name__ == "__main__":
    main()