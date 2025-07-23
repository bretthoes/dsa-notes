"""
Prim's (Minimum spanning tree)

When we learned about the basics of trees, we learned that trees at their basic are UNDIRECTED, CONNECTED, ACYCLICAL (no cycles), GRAPHS.

But what exactly is a minimum spanning tree?
Given a graph, we want to take a subset of the edges that form a tree based on the criteria on line 3, while doing it with the lowest cost possible.
Suppose we have the following simple graph:
A <- 1 -> B
B <- 2 -> C
A <- 3 -> C

To create a minimum spanning tree, we can simply remove the edge from A <-> C.
After this, the graph is still undirected and connected, but now it is also acylical, and we did it by removing the most expensive edge.
By removing this edge, the total cost of the remaining graph is 3 (1 + 2).

Note: To connect n nodes, you will need n-1 edges
Note: For a minimum spanning tree, it doesn't matter which node you start at (since you're going to need to include every node regardless)

We can run Prim's algorithm to find out multiple things, such as:
1. Cost of the minimum spanning tree
2. Return the minimum spanning tree itself, as another graph, or a list of edges
"""
 

