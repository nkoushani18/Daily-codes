import math

class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0] * (4*n)
        self.lazy = [0] * (4*n)
        self.build_tree(1, 0, n-1, arr)

    def build_tree(self, node, start, end, arr):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build_tree(node*2, start, mid, arr)
        self.build_tree(node*2+1, mid+1, end, arr)
        self.tree[node] = min(self.tree[node*2], self.tree[node*2+1])

    def update_value(self, node, start, end, left, right, val):
        if left > end or right < start:
            return
        if left <= start and end <= right:
            self.lazy[node] += val
            return
        mid = (start + end) // 2
        self.update_value(node*2, start, mid, left, right, val)
        self.update_value(node*2+1, mid+1, end, left, right, val)
        self.tree[node] = min(self.tree[node*2], self.tree[node*2+1]) + self.lazy[node]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return math.inf
        if left <= start and end <= right:
            return self.tree[node] - self.lazy[node]
        mid = (start + end) // 2
        left_val = self.query(node*2, start, mid, left, right)
        right_val = self.query(node*2+1, mid+1, end, left, right)
        return min(left_val, right_val)

# Example usage:
arr = [3, 2, 7, 5, 6]
tree = SegmentTree(arr)
print("Minimum value at index 0-4 is", tree.query(1, 0, len(arr)-1, 0, 4))

tree.update_value(1, 0, len(arr)-1, 2, 3, 10)
print("Minimum value at index 0-4 after update is", tree.query(1, 0, len(arr)-1, 0, 4))