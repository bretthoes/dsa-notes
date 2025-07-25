"""
Topological Sort
    A
  /   \
 B     C
 |     |
 D     E
  \\  /
    F
*assume above graph is directed, with every edge pointing downwards.

Looking at the above graph, we know that A must come first because it doesnt have any incoming edges.
We also know that F must come last because it doesn't have any outgoing edges.
We know that C comes before E because C has an outgoing edge to E.
We then also know implicitly that A comes before E, because A has an outgoing edge to C.

Let's say we want to add a component to the above graph, G -> H.
We now have a disjointed set and want to join these two together while maintaining alphabetical order.

We can do this with BFS or DFS.

DFS:
Run DFS on each of our two components..
Start at A, adding each node to a list (don't add duplicates):
[A,B,D,F,C,E]
Then, let's start at G for our 2nd component we're adding, adding to the same list, we end up with...:
[A,B,D,F,C,E,G,H]

This is a problem! Many of these values are not in valid order.

When we added F, we reached it using DFS, and so we hadn't yet added all incoming nodes to F, messing up our sort order.

How to solve?
Start at the beginning of the component, but dont add this node just yet.
Add all its descendents first! Do this recursively.
[F,D,B,E,C,A]
Now for our next component...
[F,D,B,E,C,A,H,G]
Now reverse the list...
[G,H,A,C,E,B,D,F]
Voila! (Relative order of components doesn't matter for topological sort, it's just about the direction)

One last catch:
What if we didn't know the beginning node of each component?
As long as we have a list of every node in the input graph, we can solve this problem by just running DFS on each node.
As long as we keep track of what's visited and don't add duplicates, it won't matter if we start at the beginning or not.
Even if there are multiple components (disjointed), this will still be fine - we may end up inserting a component in the
middle of another, but this will still be topologically valid. In the above example, we don't care if [G,H] appears in
the beginning, middle, or end of the array, just that G comes before H.
"""
def topologicalSort(edges, n):
    def dfs(src):
        if src in visited:
            return
        visited.add(src)
        # recursively visit all neighbors
        for dst in adj[src]:
            dfs(dst)
        # after visting all descendants, add this node to the result
        result.append(src)

    # build adjacency list
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for src, dst in edges:
        adj[src].append(dst)
    
    result = []
    visited = set()
    for i in range(1, n + 1):
        dfs(i)
    
    return result[::-1]


if __name__ == "__main__":
    # Example graph: 6 nodes, directed edges
    edges = [
        (1, 2),
        (1, 3),
        (2, 4),
        (4, 6),
        (5, 6),
        (3, 5),
        (7, 8)
    ]
    n = 8  # Nodes 1 to 6

    result = topologicalSort(edges, n)
    print("Topological Sort Result:", result)



