"""
dijkstra's Algorithm (shortest path)
BFS is not sufficient for finding the shortest path between two nodes when the edges have weights.
i.e., if we have the graph below and we want the shortest path from 'a' to 'd':
    a -> b
    a -> c
    a -> d
    c -> d

The SHORTEST path is just a -> d, but what if we add weights to the edges?
    a -1-> b
    a -1-> c
    a -5-> d
    c -2-> d

The "shortest" or most efficient path is now a -> c then c -> d, even though it involves more traversals.
This is where dijkstra's comes in.

The idea behind dijkstra's is having a "frontier" of nodes that we've visited so far,
and we're tracking the shortest path to these nodes so far.
and among that frontier, we want to consider all the outgoing edges,
and what the shortest path is - not just for the cost of the next jump, but the total cost from the start
to the next node.
This is where we'll use a minheap to help track.
We have a minheap where we have a pair of values <cost, node>
"""
import heapq

def shortestPath(edges, n, src):
    """
    Give na connected graph represented by a list of edges, where:
    - edge[0] = src
    - edge[1] = dest
    - edge[2] = weight,
    find the shortest path from src to every other node in the graph.
    O(E * logV), or O(E * logE)
    """
    adj = {}
    for i in range(n):
        adj[i] = []

    # s = src, d = dst, w = weight
    for s, d, w in edges:
        adj[s].append((w,d))

    shortest = {}
    heap = [(0, src)]
    while heap:
        weight, node = heapq.heappop(heap)
        if node in shortest:
            continue
        shortest[node] = weight

        for neighborWeight, neighbor in adj[node]:
            if neighbor not in shortest:
                heapq.heappush(heap, (weight + neighborWeight, neighbor))

    return shortest


edges = [
    (0, 1, 4),
    (0, 2, 1),
    (1, 2, 2),
    (1, 3, 1),
    (2, 3, 5),
]
n   = 4
src = 0

# call your function
print(shortestPath(edges, n, src))
"""
    (0)
   /   \
  4     1
 /       \
(1)———2——>(2)
  |      /
  1     5
  |   /
  (3)
"""
