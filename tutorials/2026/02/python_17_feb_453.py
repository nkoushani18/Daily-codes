# Topological Sort in Python
=====================================

Topological sorting is an ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering.

```python
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    # Add an edge between two vertices
    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)

    # Perform topological sort using DFS and a stack
    def topological_sort(self):
        visited = [False] * self.num_vertices
        stack = []

        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                self._dfs(vertex, visited, stack)

        return stack

    # Recursive helper function to perform DFS
    def _dfs(self, vertex, visited, stack):
        visited[vertex] = True

        # Visit all neighbors of the current vertex
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        
        # Push the current vertex onto the stack after visiting all its neighbors
        stack.append(vertex)


# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)

    # Perform topological sort
    sorted_vertices = g.topological_sort()
    print("Topologically Sorted Vertices:", sorted_vertices)