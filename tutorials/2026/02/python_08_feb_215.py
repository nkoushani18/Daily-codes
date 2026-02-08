# Dijkstra's Shortest Path Algorithm in Python
==============================================

### Overview

Dijkstra's algorithm is a well-known algorithm for finding the shortest path between nodes in a graph.

### Code

```python
import sys
import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm to find the shortest path from start node to all other nodes.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph.
    start (node): Starting node for the search.
    
    Returns:
    distances (dict): Shortest distance from start node to all other nodes.
    previous (dict): Previous node in the shortest path.
    """
    # Initialize distances and previous dictionaries
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    # Priority queue to hold nodes to be processed
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the already found distance, skip this node
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update its distance and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


def shortest_path(graph, start, end):
    """
    Find the shortest path from start node to end node.
    
    Parameters:
    graph (dict): Adjacency list representation of the graph.
    start (node): Starting node for the search.
    end (node): Ending node for the search.
    
    Returns:
    path (list): Shortest path from start node to end node.
    """
    distances, previous = dijkstra(graph, start)

    # Build the shortest path by backtracking from end node
    current_node = end
    path = []
    while current_node is not None:
        path.append(current_node)
        current_node = previous[current_node]

    return list(reversed(path))


# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'

distances, previous = dijkstra(graph, start_node)
print("Shortest distances from {}:".format(start_node))
for node in graph:
    print("{}: {}".format(node, distances[node]))

path = shortest_path(graph, start_node, end_node)
print("\nShortest path from {} to {}: {}".format(start_node, end_node, ' -> '.join(path)))