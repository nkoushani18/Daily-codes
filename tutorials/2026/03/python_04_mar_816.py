from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1

    def topological_sort(self):
        # Initialize a queue to store vertices with in-degree 0
        queue = deque()
        for i in range(self.V):
            if self.in_degree[i] == 0:
                queue.append(i)

        # Initialize an empty list to store the sorted vertices
        sorted_vertices = []

        # Perform topological sort
        while queue:
            vertex = queue.popleft()
            sorted_vertices.append(vertex)

            for neighbour in self.graph[vertex]:
                self.in_degree[neighbour] -= 1
                if self.in_degree[neighbour] == 0:
                    queue.append(neighbour)

        # If there are still vertices with in-degree greater than 0, 
        # then the graph contains a cycle and topological sort is not possible
        if len(sorted_vertices) != self.V:
            print("Graph contains a cycle and topological sort is not possible.")
            return None

        return sorted_vertices

# Example usage
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

sorted_vertices = g.topological_sort()
if sorted_vertices:
    print("Topological Sort:", sorted_vertices)