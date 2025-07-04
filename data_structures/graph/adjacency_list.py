from collections import deque


class GraphNode:
    def __init__(self, value) -> None:
        self.value = value
        self.neighbors = []

edges = [["A", "B"],
         ["B", "C"],
         ["B", "E"],
         ["C", "E"],
         ["E", "D"]]

adj_list = {}

for src, dest in edges:
    if src not in adj_list:
        adj_list[src] = []
    adj_list[src].append(dest)

# count paths (backtracking)
def dfs(node, target, adjList, visited: set):
    if node in visited:
        return 0
    if node == target:
        return 1

    count = 0
    visited.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visited)
    visited.remove(node)

    return count

print(dfs("A", "E", adj_list, set()))

# shortest path from node to target
def bfs(node, target, adjList, visited: set):
    queue = deque()
    queue.append(node)
    visited.add(node)
    count = 0
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur in visited:
                continue
            if cur == target:
                return count
            for neighbor in adjList[cur]:
                queue.append(neighbor)
                visited.add(neighbor)
        count += 1
    return count





print(bfs("A", "E", adj_list, set()))





