# Topological Sort using Depth First Search (DFS)

class Graph:
    def __init__(self, vertices):
        # Initialize the graph with the given number of vertices
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Add an edge between two vertices
        self.graph[u].append(v)

    def topological_sort_util(self, vertex, visited, stack):
        # Recursive utility function to perform DFS

        # Mark the current vertex as visited
        visited[vertex] = True

        # Recur for all adjacent vertices of the current vertex
        for neighbour in self.graph[vertex]:
            if not visited[neighbour]:
                self.topological_sort_util(neighbour, visited, stack)
        
        # Push the current vertex to the stack
        stack.insert(0, vertex)

    def topological_sort(self):
        # Perform DFS traversal and store sorted vertices in a list
        visited = [False] * (self.V + 1)  
        stack = [] 

        for i in range(self.V): 
            if not visited[i]: 
                self.topological_sort_util(i, visited, stack)
        
        return stack

# Test the topological sort function
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

sorted_vertices = g.topological_sort()
print("Topologically sorted vertices: ", end='')
print(*sorted_vertices)