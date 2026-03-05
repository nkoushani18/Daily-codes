class UnionFind:
    def __init__(self, n):
        # Initialize the parent array to store the parent of each node
        self.parent = list(range(n))
        # Initialize the rank array to store the rank of each node
        self.rank = [0] * n

    def find(self, x):
        # If x is not the parent of itself, find its parent
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        # Return the parent of x
        return self.parent[x]

    def union(self, x, y):
        # Find the parents of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        # If root_x and root_y are different, perform union
        if root_x != root_y:
            # If the rank of root_x is less than the rank of root_y, make root_y the parent of root_x
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            # If the rank of root_x is greater than the rank of root_y, make root_x the parent of root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            # If the ranks are equal, make root_x the parent of root_y and increment the rank of root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        # Return True if x and y are in the same set, False otherwise
        return self.find(x) == self.find(y)


# Example usage
if __name__ == "__main__":
    n = 5
    uf = UnionFind(n)
    # Perform union operations
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    # Check connectedness
    print(uf.connected(0, 1))  # Output: True
    print(uf.connected(0, 3))  # Output: False