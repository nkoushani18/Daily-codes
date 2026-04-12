# Dijkstra's Shortest Path Algorithm Implementation in Python

import sys
import heapq

def dijkstra(graph, start_node):
    """
    Finds the shortest path from the start node to all other nodes in the graph.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph.
    start_node: Node to start the search from.
    
    Returns:
    distances (dict): Shortest distance from the start node to each other node.
    previous_nodes (dict): Previous node in the shortest path from the start node.
    """
    # Initialize distances and previous nodes dictionaries
    distances = {node: sys.maxsize for node in graph}
    distances[start_node] = 0
    previous_nodes = {node: None for node in graph}

    # Priority queue to hold nodes to be processed
    priority_queue = [(0, start_node)]

    while priority_queue:
        # Extract the node with the minimum distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the extracted distance is greater than the known distance, skip this node
        if current_distance > distances[current_node]:
            continue

        # Iterate over all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update its distance and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)

print("Shortest distances from", start_node)
for node in graph:
    print(node, ":", distances[node])

print("\nPrevious nodes in the shortest path")
for node in graph:
    print(node, ":", previous_nodes[node])
```

To run this code, create a new Python file (e.g., `dijkstra.py`) and paste the above code into it. Then, open a terminal or command prompt, navigate to the directory containing your Python file, and execute it using the following command:

```bash
python dijkstra.py