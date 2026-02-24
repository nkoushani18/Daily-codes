class UnionFind:
    def __init__(self, n):
        # Initialize parent array
        self.parent = list(range(n))
        # Initialize rank array
        self.rank = [0] * n

    def find(self, x):
        # If x is not the root, find the root and update the parent
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        # If the roots are the same, no need to union
        if root_x == root_y:
            return
        # If the rank of root_x is less than the rank of root_y, make root_y the root
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        # If the rank of root_x is greater than the rank of root_y, make root_x the root
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        # If the ranks are the same, make one root and increment the rank
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

# Test the UnionFind class
if __name__ == "__main__":
    n = 10
    uf = UnionFind(n)
    print("Initial Parent Array:")
    print(uf.parent)
    print("Initial Rank Array:")
    print(uf.rank)
    # Union some nodes
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    print("\nAfter Union:")
    print("Parent Array:")
    print(uf.parent)
    print("Rank Array:")
    print(uf.rank)
    # Find the root of a node
    print("\nFind Root of Node 0:")
    print(uf.find(0))
    # Check if two nodes are in the same set
    print("\nAre 0 and 1 in the same set?")
    print(uf.find(0) == uf.find(1))
    # Union some more nodes
    uf.union(5, 6)
    uf.union(7, 8)
    print("\nAfter More Union:")
    print("Parent Array:")
    print(uf.parent)
    print("Rank Array:")
    print(uf.rank)