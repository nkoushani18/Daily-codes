class UnionFind:
    def __init__(self, n):
        """
        Initializes the UnionFind class with a given number of elements.
        
        :param n: The number of elements in the set.
        """
        # Each element is initially in its own separate set.
        self.parent = list(range(n))
        # The rank of each element's set is initially 0.
        self.rank = [0] * n

    def find(self, x):
        """
        Finds the root of the set that contains x.
        
        :param x: An element in the set.
        :return: The root of the set that contains x.
        """
        # If x is not the root of its set, then it must be in a different set.
        if self.parent[x] != x:
            # Find the root of the set and attach x to it.
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Merges the sets that contain x and y.
        
        :param x: An element in the first set.
        :param y: An element in the second set.
        """
        # Find the roots of the sets that contain x and y.
        root_x = self.find(x)
        root_y = self.find(y)

        # If the roots are different, then the sets must be separate.
        if root_x != root_y:
            # Attach one set to the other.
            if self.rank[root_x] > self.rank[root_y]:
                # If the rank of x's set is higher, attach y's set to it.
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                # If the rank of y's set is higher, attach x's set to it.
                self.parent[root_x] = root_y
            else:
                # If the ranks are equal, then attach one set to the other and increment its rank.
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


# Example usage:

if __name__ == "__main__":
    uf = UnionFind(10)
    print("Initial sets:")
    for i in range(10):
        print(f"{i} -> {uf.find(i)}")

    # Merge two sets.
    uf.union(0, 5)
    print("\nAfter merging (0, 5):")
    for i in range(10):
        print(f"{i} -> {uf.find(i)}")

    # Check that the merge worked correctly.
    assert uf.find(0) == uf.find(5), "Sets did not merge correctly"

    # Merge another set.
    uf.union(8, 9)
    print("\nAfter merging (8, 9):")
    for i in range(10):
        print(f"{i} -> {uf.find(i)}")

    # Check that the second merge worked correctly.
    assert uf.find(0) == uf.find(5), "Sets did not merge correctly"
    assert uf.find(8) == uf.find(9), "Sets did not merge correctly"