"""
Djikstra's Algorithm (shortest path)
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
This is where Djikstra's comes in.

The idea behind Djikstra's is having a "frontier" of nodes that we've visited so far,
and we're tracking the shortest path to these nodes so far.
and among that frontier, we want to consider all the outgoing edges,
and what the shortest path is - not just for the cost of the next jump, but the total cost from the start
to the next node.
This is where we'll use a minheap to help track.
We have a minheap where we have a pair of values <cost, node>
"""

