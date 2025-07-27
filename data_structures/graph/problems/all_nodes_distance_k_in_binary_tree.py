from collections import defaultdict, deque
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # attempt 2 -> k nearest, graph, adj list
        # approach ->
        # iterate thru tree
        # treat edges as undirected (need to track prev)
        # create a queue, add target, process all neighbors
        # go to all neighbors k distance away, return all these
        def _dfs(root, prev, adj):
            if not root:
                return
            if prev and prev not in adj[root]:
                adj[root.val].add(prev.val)
            if root.left:
                adj[root.val].add(root.left.val)
            if root.right:
                adj[root.val].add(root.right.val)
            
            _dfs(root.left, root, adj)
            _dfs(root.right, root, adj)

        # build adj list
        adj = defaultdict(set)
        _dfs(root, None, adj)
        
        q = deque()
        q.append(target.val)
        count = 0
        visited = set()
        while q:
            if count == k:
                return list(q)
            # layer by layer
            for _ in range(len(q)):
                popped = q.popleft()
                visited.add(popped)
                for neighbor in adj[popped]:
                    if neighbor not in visited:
                        q.append(neighbor)
            count += 1
        return []

                    




        
