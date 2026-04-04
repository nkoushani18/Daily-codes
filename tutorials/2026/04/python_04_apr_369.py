# Topological Sort in Python

class Graph:
    def __init__(self):
        self.graph = {}

    # Function to add an edge between two vertices
    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    # Function to check for cycles using DFS
    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.is_cyclic_util(neighbor, visited, rec_stack) == True:
                    return True
            elif rec_stack[neighbor] == True:
                return True

        rec_stack[v] = False
        return False

    # Function to check for cycles
    def is_cyclic(self):
        visited = {}
        rec_stack = {}

        for node in self.graph:
            if visited[node] == False:
                if self.is_cyclic_util(node, visited, rec_stack) == True:
                    return True
        return False

    # Topological Sort using Kahn's Algorithm
    def topological_sort(self):
        if self.is_cyclic() == True:
            print("Graph contains cycle")
            return None

        sorted_nodes = []
        queue = []

        for node in self.graph:
            if len(self.graph[node]) == 0:
                queue.append(node)

        while len(queue) > 0:
            node = queue.pop(0)
            sorted_nodes.append(node)

            for neighbor in reversed(self.graph[node]):
                self.graph[neighbor].remove(node)
                if len(self.graph[neighbor]) == 0:
                    queue.append(neighbor)

        return sorted_nodes


# Example usage
g1 = Graph()
g1.add_edge('A', 'B')
g1.add_edge('B', 'C')
g1.add_edge('C', 'D')

print("Topological Sort for graph with cycles:")
print(g1.topological_sort())

g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('B', 'C')
g2.add_edge('C', 'D')
g2.add_edge('D', 'E')

print("\nTopological Sort for graph without cycles:")
print(g2.topological_sort())