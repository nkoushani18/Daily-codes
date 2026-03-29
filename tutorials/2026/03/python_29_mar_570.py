# Union-Find Algorithm Implementation in Python

class UnionFind:
    def __init__(self, n):
        """
        Initialize the union-find data structure with 'n' elements.
        
        :param n: The number of elements in the set.
        """
        # Each element is initially in its own set.
        self.parent = list(range(n))
        # Each element's rank is 0.
        self.rank = [0] * n

    def find(self, x):
        """
        Find the root of the set that contains 'x'.
        
        :param x: The element to find the root for.
        :return: The root of the set containing 'x'.
        """
        # If 'x' is not its own parent, it's in a different set.
        if self.parent[x] != x:
            # Use path compression to optimize future find operations.
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Merge the sets containing 'x' and 'y'.
        
        :param x: The first element in the sets.
        :param y: The second element in the sets.
        """
        # Find the roots of the sets containing 'x' and 'y'.
        root_x = self.find(x)
        root_y = self.find(y)

        # If the roots are different, merge the sets.
        if root_x != root_y:
            # Use union by rank to optimize future operations.
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                # Increment the rank of the winning set's parent.
                self.rank[root_x] += 1

# Example usage:
if __name__ == "__main__":
    uf = UnionFind(5)
    print("Initial sets:")
    for i in range(5):
        print(f"{i} -> {uf.find(i)}")

    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 0)

    print("\nAfter union operations:")
    for i in range(5):
        print(f"{i} -> {uf.find(i)}")