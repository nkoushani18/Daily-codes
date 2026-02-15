class UnionFind:
    def __init__(self, size):
        """
        Initialize the union-find data structure with a specified size.

        :param size: The number of elements in the set.
        """
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        """
        Find the root of the set that contains element x.

        :param x: The element to find the root for.
        :return: The root of the set containing x.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Merge the sets that contain elements x and y.

        :param x: An element in the first set.
        :param y: An element in the second set.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                # x is the parent of y, so promote y to be the parent
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                # y is the parent of x, so promote x to be the parent
                self.parent[root_x] = root_y
            else:
                # Both roots have the same rank, so we need a tiebreaker
                # Increment the rank of both roots and make one of them the parent
                self.rank[root_x] += 1
                self.parent[root_y] = root_x

def union_find_example():
    uf = UnionFind(10)
    
    print("Initial sets:")
    for i in range(10):
        print(f"Set {i}: {uf.find(i)}")

    # Merge some sets
    uf.union(0, 1)
    uf.union(2, 3)

    print("\nSets after merge:")
    for i in range(10):
        print(f"Set {i}: {uf.find(i)}")

union_find_example()