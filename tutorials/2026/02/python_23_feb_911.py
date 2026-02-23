class UnionFind:
    def __init__(self, n):
        # Initialize parent array with each element as itself
        self.parent = list(range(n))
        # Initialize rank array with each element as 0
        self.rank = [0]*n

    def find(self, x):
        # If x is not the parent of itself, find its root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find roots of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        # If roots are the same, return
        if root_x == root_y:
            return
        # If rank of root_x is greater, make root_y child of root_x
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        # If rank of root_y is greater, make root_x child of root_y
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        # If ranks are equal, make root_y child of root_x and increment rank of root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def connected(self, x, y):
        # Return True if x and y are in the same set, False otherwise
        return self.find(x) == self.find(y)


# Test the UnionFind class
if __name__ == "__main__":
    # Create an instance of UnionFind with 5 elements
    uf = UnionFind(5)
    # Perform some unions
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    # Check if some elements are connected
    print(uf.connected(0, 1))  # Output: True
    print(uf.connected(0, 2))  # Output: False
    print(uf.connected(3, 4))  # Output: True
    # Check if some elements are not connected
    print(uf.connected(0, 3))  # Output: False
    print(uf.connected(1, 4))  # Output: False