class QuickUnion:
    def __init__(self, n):
        self.n = n
        self.id = list(range(n))  # Initialize each element as its own root

    def _root(self, i):
        """
        Private helper method to find the root of a given element.
        """
        while i != self.id[i]:
            i = self.id[i]
        return i

    def union(self, p, q):
        """
        Union operation: Connects two elements by making the root of one element point to the root of the other element.
        """
        p_root = self._root(p)
        q_root = self._root(q)

        # If the elements are already in the same set, do nothing
        if p_root == q_root:
            return

        # Connect the root of p to the root of q
        self.id[p_root] = q_root

    def connected(self, p, q):
        """
        Connected operation: Checks if two elements are connected (i.e., they have the same root).
        """
        return self._root(p) == self._root(q)


# Example usage:
n = 10  # Number of elements in the set
uf = QuickUnion(n)

uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)
uf.union(8, 9)

print(uf.connected(0, 1))  # Should print True
print(uf.connected(0, 2))  # Should print False
