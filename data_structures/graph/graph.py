"""
# Graph Representations & Terminology

## 1. Basic Definitions

- Graph: A collection of vertices (nodes) and edges (connections) between them.

- Vertex (Node): An individual element or “point” in the graph.

- Edge: A connection between two vertices. Can be directed or undirected; can carry a weight or be unweighted.

- Directed vs. Undirected:
  - Directed Graph (Digraph): Edges have a direction; an edge (u → v) allows traversal from u to v but not necessarily from v to u.
  - Undirected Graph: Edges are bidirectional; an edge {u, v} means you can traverse between u and v in both directions.

- Weighted vs. Unweighted:
  - Weighted Graph: Each edge has a weight/cost. Useful for shortest-path algorithms (e.g., Dijkstra).
  - Unweighted Graph: All edges are “equal”; often treated as weight = 1 implicitly.

- Self-loop: An edge from a vertex to itself.

- Parallel edges (Multigraph): Multiple edges between the same pair of vertices. (Often graphs in algorithm problems assume simple graphs without parallel edges or loops.)

- Cycle: A path that starts and ends at the same vertex without repeating edges (and typically without repeating other vertices, depending on definition).

- Path: A sequence of vertices connected by edges. A simple path does not repeat vertices.

- Connectedness (for undirected graphs):
  - Connected graph: There is a path between every pair of vertices.
  - Connected component: A maximal set of vertices where each pair is reachable.

- Strongly/Weakly Connected (for directed graphs):
  - Strongly connected: For every pair (u, v), there is a directed path u→…→v and v→…→u.
  - Weakly connected: If, when ignoring edge directions, the underlying undirected graph is connected.

- Acyclic, DAG:
  - Acyclic: No cycles.
  - Directed Acyclic Graph (DAG): Directed graph with no directed cycles. Important for topological sort.

- Degree:
  - Undirected: Number of edges incident to a vertex.
  - Directed: 
    - In-degree: Number of incoming edges to a vertex.
    - Out-degree: Number of outgoing edges from a vertex.


## 2. Graph Representations

### 2.1 Adjacency Matrix
- A 2D array `adj` of size V × V (where V = number of vertices).
- For unweighted graphs: `adj[u][v] = 1` if there is an edge u→v (or edge between u and v, for undirected), else 0.
- For weighted graphs: `adj[u][v] = weight` if edge exists, else some sentinel (e.g., `inf` or 0 if 0 means no edge).
- Pros:
  - O(1) check “is there an edge between u and v?”
  - Simple to implement.
- Cons:
  - Space: O(V²) even if few edges (sparse graphs waste memory).
  - Iterating neighbors of u takes O(V) (scan row) even if u has few neighbors.
- Use when: Graph is dense (number of edges E is close to V²), or V is small enough that V² is acceptable.

### 2.2 Adjacency List
- An array (or dict) of length V, where each entry stores a list of neighbors:
  - For vertex u, store a list/array of (v[, weight]) for each edge u→v.
- Pros:
  - Space: O(V + E). Good for sparse graphs.
  - Iterating neighbors of u is O(degree(u)), efficient when degree is small.
- Cons:
  - Checking existence of a specific edge (u, v) may be O(degree(u)) unless additional data structures (e.g., hash set) are used.
- Use when: Graph is sparse (E ≪ V²), which is common in many problems.

### 2.3 Other Representations (less common in basic algorithms)
- Edge List: A list of edges [(u, v[, weight]), ...]. Useful for algorithms like Kruskal’s MST (you sort edges).
- Incidence Matrix: A V × E matrix indicating which vertices are incident to which edges. Rarely used in typical algorithm problems.
- Compressed/Specialized Structures: For very large graphs, one may use CSR (Compressed Sparse Row) or other memory-efficient formats.

## 3. Key Operations & Complexities

- Build adjacency structure:

  - From a list of edges: 
    - Adjacency list: For each edge, append neighbor → O(E) time, O(V+E) space (assuming V known or implicitly sized).
    - Adjacency matrix: Initialize V×V array → O(V²), then for each edge set entry → O(E).

- Traversal:

  - BFS (Breadth-First Search):
    - Use a queue.
    - Visits vertices in “layers” from a source.
    - Time: O(V + E) with adjacency list; O(V²) with adjacency matrix.
    - Finds shortest path (fewest edges) in unweighted graph.

  - DFS (Depth-First Search):
    - Use recursion or explicit stack.
    - Time: O(V + E) with adjacency list; O(V²) with adjacency matrix.
    - Useful for detecting cycles, topological sort (on DAG), connectivity, etc.

- Shortest Paths:
  - Unweighted: BFS from source gives shortest in O(V + E).
  - Weighted (non-negative weights): Dijkstra with a min-heap: O((V + E) log V) or O(E log V) depending on representation.
  - Negative weights / detect negative cycles: Bellman-Ford O(V E).

- MST (Minimum Spanning Tree) (undirected weighted):
  - Kruskal’s: sort edges O(E log E) then union-find.
  - Prim’s: with adjacency list + min-heap O(E log V).

- Topological Sort (DAG):
  - Kahn’s algorithm (BFS-like, in-degree tracking): O(V + E).
  - DFS-based: O(V + E).

- Connected Components:
  - Undirected: Repeated BFS/DFS to mark components: O(V + E).
  - Directed: Strongly connected components (Kosaraju’s, Tarjan’s) in O(V + E).

- Cycle Detection:
  - Undirected: DFS tracking parent or Union-Find on edges.
  - Directed: DFS with recursion stack or Kahn’s algorithm (if topological sort doesn’t include all vertices, there’s a cycle).

"""

from collections import deque


class GraphNode:
    def __init__(self, value) -> None:
        self.value = value
        self.neighbors = []


