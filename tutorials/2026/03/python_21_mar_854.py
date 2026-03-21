# Topological Sort in Python
# ===========================

class Graph:
    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Add a new vertex to the graph.

        :param vertex: The vertex to be added.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Add an edge between two vertices.

        :param vertex1: The first vertex.
        :param vertex2: The second vertex.
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)

    def topological_sort(self):
        """
        Perform a topological sort on the graph.

        :return: A list of vertices in topological order.
        """
        visited = set()
        stack = []

        for vertex in self.graph:
            if vertex not in visited:
                self._dfs(vertex, visited, stack)

        return stack

    def _dfs(self, vertex, visited, stack):
        """
        Perform a depth-first search on the graph.

        :param vertex: The current vertex.
        :param visited: A set of visited vertices.
        :param stack: A list to store the sorted vertices.
        """
        visited.add(vertex)

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)
        stack.append(vertex)


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")

    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "D")
    g.add_edge("D", "A")

    print("Topological Sort:")
    for vertex in g.topological_sort():
        print(vertex)