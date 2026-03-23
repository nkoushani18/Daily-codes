class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    # Find the root of a set that contains an element
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union two sets into one
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        # If both elements are already in the same set, do nothing
        if root_x == root_y:
            return

        # Attach smaller set to the parent of larger set
        if len(self.parent[root_x]) < len(self.parent[root_y]):
            self.parent[root_x] += self.parent[root_y]
            self.parent[root_y] = root_x
        elif len(self.parent[root_x]) > len(self.parent[root_y]):
            self.parent[root_y] += self.parent[root_x]
            self.parent[root_x] = root_y

    # Check if two elements are in the same set
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Example usage of union-find algorithm
if __name__ == "__main__":
    uf = UnionFind(6)
    print("Initial groups:", [uf.find(i) for i in range(1, 7)])

    # Divide into two sets
    uf.union(0, 1)
    uf.union(2, 3)

    # Check if some elements are in the same group
    print("Are 0 and 1 in the same group?", uf.connected(0, 1))
    print("Are 1 and 2 in the same group?", uf.connected(1, 2))

    # Divide into three sets
    uf.union(4, 5)

    # Check if some elements are in the same group
    print("Are 3 and 4 in the same group?", uf.connected(3, 4))