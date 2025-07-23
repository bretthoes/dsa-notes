"""
Kruskal's (Minimum Spanning Tree)
An easier way to create an MST using UnionFind
"""
import heapq

from data_structures.union_find import UnionFind

def kruskals(edges, n):
    """
    Given a list of edges of a connected undirected graph,
    with nodes fron 1 to n, return a list of edges making
    up the minimum spanning tree.
    """
    heap = []
    for n1, n2, weight in edges:
        heapq.heappush(heap, [weight, n1, n2])

    uf = UnionFind()
    mst = []
    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(heap)
        if not uf.union(n1, n2):
            continue
        mst.append([n1, n2])
    return mst

