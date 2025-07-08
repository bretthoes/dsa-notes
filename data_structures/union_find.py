class UnionFind:
    """
    Data Structure: UnionFind
    Alternate Names: DisjointSet, DisjointSetUnion (DSU)
    
    Description:
        Maintains a partition of a set into disjoint subsets, allowing
        efficient union and find operations to track connected components
        or equivalence classes.
    
    Supported Operations:
        • make_set(element) -> None
            – Purpose: Create a new singleton set containing `element`.
            – Time Complexity: amortized O(1)
        • find(element) -> Representative
            – Purpose: Return the representative (root) of the set containing `element`.
            – Time Complexity: near‐constant (inverse Ackermann α(n))
        • union(a, b) -> None
            – Purpose: Merge the sets containing `a` and `b`.
            – Time Complexity: near‐constant (α(n))
    
    Usage Examples:
        uf = UnionFind()
        uf.make_set("x")
        uf.make_set("y")
        uf.union("x", "y")
        rep_x = uf.find("x")  # same as uf.find("y")
    
    Implementation Details:
        • Internal storage:
            – parent: dict mapping element → parent element
            – rank: dict mapping element → tree depth approximation
        • Optimizations:
            – Path compression in `find`
            – Union by rank in `union`
        • Concurrency:
            – Not thread-safe; external synchronization required if used from multiple threads
    
    Edge Cases & Error Handling:
        • Accessing unknown element: `find` or `union` on a missing element raises KeyError
        • Duplicate `make_set`: raises KeyError (element already present)
    
    References:
        • Cormen, Leiserson, Rivest, Stein – “Introduction to Algorithms,” Section on Disjoint Sets
        • Tarjan – “Efficiency of a Good but Not Linear Set Union Algorithm”
    """

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, element):
        """Initialize `element` in its own set."""
        if element in self.parent:
            raise KeyError(f"{element!r} already exists")
        self.parent[element] = element
        self.rank[element] = 0

    def find(self, element):
        """Find and return the set representative for `element`, applying path compression."""
        if element not in self.parent:
            raise KeyError(f"{element!r} not found")
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, a, b):
        """Union the sets containing `a` and `b` by rank."""
        ra, rb = self.find(a), self.find(b)

        # early return if the two nodes belong to the same component already
        if ra == rb:
            return

        # If root A’s tree is taller, attach B under A
        if self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra

        # If root B’s tree is taller, attach A under B
        elif self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb

        # If both trees have the same rank, pick A as new root
        # and increment its rank by 1
        else:
            self.parent[rb] = ra
            # Note: we only increment rank in the case where they are equal because if we are
            # attaching a shorter tree to a longer one, it does not change either rank
            self.rank[ra] += 1

# Suppose we start with:
uf = UnionFind()
for x in ["A", "B", "C", "D", "E"]:
    uf.make_set(x)

# Now every element is its own parent:
uf.parent
# {
#   "A": "A",
#   "B": "B",
#   "C": "C",
#   "D": "D",
#   "E": "E",
# }

uf.rank
# {
#   "A": 0,
#   "B": 0,
#   "C": 0,
#   "D": 0,
#   "E": 0,
# }

# Perform some unions:
uf.union("A", "B")
uf.union("C", "D")
uf.union("B", "C")   # this merges the {A,B} and {C,D} sets

# After path-compressed finds, the maps might look like:
uf.parent
# {
#   "A": "A",    # root of the big set
#   "B": "A",    # B’s parent is now A
#   "C": "A",    # C was under D or C, but path-compressed to A
#   "D": "C",    # D’s parent still points to C (but find(D) → C → A)
#   "E": "E",    # still in its own singleton set
# }

uf.rank
# {
#   "A": 2,      # A’s tree is now height ≈2
#   "B": 0,
#   "C": 1,      # C’s subtree (just D) is height 1
#   "D": 0,
#   "E": 0,
# }
