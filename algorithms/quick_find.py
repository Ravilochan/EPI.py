class QuickFind:
    def __init__(self, n):
        self.n = n
        # Initialize each element with its own identifier
        self.id = list(range(n))

    def union(self, p, q):
        """
        Union operation: Connects two elements by changing the identifier of all elements in one set to match the other.
        """
        p_id = self.id[p]
        q_id = self.id[q]

        # If the elements are already in the same set, do nothing
        if p_id == q_id:
            return

        # Update the identifiers of all elements in set p to match set q
        for i in range(self.n):
            if self.id[i] == p_id:
                self.id[i] = q_id

    def connected(self, p, q):
        """
        Connected operation: Checks if two elements are connected (i.e., they have the same identifier).
        """
        return self.id[p] == self.id[q]


# Example usage:
n = 10  # Number of elements in the set
uf = QuickFind(n)

uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)
uf.union(8, 9)

print(uf.connected(0, 1))  # Should print True
print(uf.connected(0, 2))  # Should print False
