# Breadth First Search (BFS) Graph Traversal in Python
=====================================================

### Overview

This code implements a Breadth First Search (BFS) algorithm for graph traversal using an adjacency list representation.

```python
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    # Function to add edge between two vertices
    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.adj_list[src] = [dest]
        else:
            self.adj_list[src].append(dest)

    # Function to perform BFS traversal starting from a given source vertex
    def bfs_traversal(self, start_vertex):
        visited = set()
        traversal_order = []
        queue = deque([start_vertex])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)

                # Add all adjacent vertices to the queue
                for neighbor in self.adj_list.get(vertex, []):
                    queue.append(neighbor)

        return traversal_order

# Example usage
if __name__ == "__main__":
    graph = Graph()

    # Adding edges between vertices
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')

    start_vertex = 'A'
    traversal_order = graph.bfs_traversal(start_vertex)

    print(f"Traversing order starting from {start_vertex}: {traversal_order}")