import collections

class Graph:
    def __init__(self):
        # Initialize an empty graph as a dictionary of lists
        self.graph = {}

    def add_edge(self, u, v):
        # Add a new edge to the graph by adding the vertex and its neighbors
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start_vertex):
        # Perform BFS traversal from the given vertex
        visited = set()
        queue = collections.deque([start_vertex])
        visited.add(start_vertex)
        
        while queue:
            vertex = queue.popleft()
            
            print(vertex, end=" ")
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def print_graph(self):
        # Print the adjacency list representation of the graph
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

# Create a graph with 5 vertices and add edges between them
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'F')
g.add_edge('D', 'E')
g.add_edge('E', 'F')

# Print the adjacency list representation of the graph
print("Adjacency List Representation:")
g.print_graph()

# Perform BFS traversal from vertex 'A'
print("\nBFS Traversal from Vertex 'A':")
g.bfs('A')