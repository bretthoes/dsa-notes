"""
Data Structure: BinaryTree
Alternate Names: BT, Ordered Binary Tree

Description:
    A binary tree is a hierarchical data structure in which each node has up to two children,
    typically referred to as the left and right child. Useful for representing hierarchical
    relationships, expression trees, and as the foundation for more advanced trees (BSTs, heaps).

Supported Operations:
    • traverse_preorder() -> List[value]
        – Purpose: Visit root, left subtree, then right subtree.
        – Time Complexity: O(n)
    • traverse_inorder() -> List[value]
        – Purpose: Visit left subtree, root, then right subtree.
        – Time Complexity: O(n)
    • traverse_postorder() -> List[value]
        – Purpose: Visit left subtree, right subtree, then root.
        – Time Complexity: O(n)
    • traverse_levelorder() -> List[value]
        – Purpose: Visit nodes level by level (breadth-first).
        – Time Complexity: O(n)
    • height() -> int
        – Purpose: Compute the maximum depth of the tree.
        – Time Complexity: O(n)
    • count_nodes() -> int
        – Purpose: Count total nodes in the tree.
        – Time Complexity: O(n)

Implementation Details:
    • Node: simple class with `value`, `left`, and `right` attributes.
    • BinaryTree: wraps the `root` and provides methods for manipulation and traversal.
    • Traversals are implemented recursively (except level-order, which uses a queue).

Edge Cases & Error Handling:
    • Inserting under None parent: raises ValueError.
    • Searching empty tree: returns None.
    • Duplicate values: search returns first match in pre-order.

References:
    • Goodrich, Tamassia, Goldwasser – “Data Structures & Algorithms in Python”
    • Wikipedia – “Binary Tree”
"""

from collections import deque
from typing import Any, List, Optional


class Node:
    """A single node in a binary tree."""
    def __init__(self, value: Any):
        self.value: Any = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class BinaryTree:
    """A basic binary tree."""
    def __init__(self, root_value: Any):
        self.root: Node = Node(root_value)

    def traverse_preorder(self) -> List[Any]:
        """Return values in pre-order: root, left, right."""
        result: List[Any] = []

        def _pre(node: Optional[Node]):
            if not node:
                return
            result.append(node.value)
            _pre(node.left)
            _pre(node.right)

        _pre(self.root)
        return result

    def traverse_inorder(self) -> List[Any]:
        """Return values in in-order: left, root, right."""
        result: List[Any] = []

        def _in(node: Optional[Node]):
            if not node:
                return
            _in(node.left)
            result.append(node.value)
            _in(node.right)

        _in(self.root)
        return result

    def traverse_postorder(self) -> List[Any]:
        """Return values in post-order: left, right, root."""
        result: List[Any] = []

        def _post(node: Optional[Node]):
            if not node:
                return
            _post(node.left)
            _post(node.right)
            result.append(node.value)

        _post(self.root)
        return result

    def traverse_levelorder(self) -> List[Any]:
        """Return values in level-order (breadth-first)."""
        result: List[Any] = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def height(self) -> int:
        """Return the height (max depth) of the tree."""
        def _height(node: Optional[Node]) -> int:
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def count_nodes(self) -> int:
        """Count total nodes in the tree."""
        def _count(node: Optional[Node]) -> int:
            if not node:
                return 0
            return 1 + _count(node.left) + _count(node.right)
        return _count(self.root)

    """
    Samples methods for learning purposes
    """
    def has_path_without_zero(self) -> bool:
        """
        Determine if there exists at least one root-to-leaf path with no node values equal to zero.
        :return: True if such a path exists, False otherwise.
        Time Complexity: O(n), where n is the number of nodes.
        """
        def _dfs(node: Optional[Node]) -> bool:
            if node is None:
                return False
            if node.value == 0:
                return False
            # If leaf node with non-zero value
            if node.left is None and node.right is None:
                return True
            # Check left subtree
            if _dfs(node.left):
                return True
            # Check right subtree
            if _dfs(node.right):
                return True
            return False
        return _dfs(self.root)

    def first_path_without_zero(self) -> List[int]:
        """
        Return a list of node values along the first root-to-leaf path found with no zeros.
        If no such path exists, return an empty list.
        Time Complexity: O(n) in the worst case (search entire tree).
        """
        path: List[int] = []
        def _dfs(node: Optional[Node]) -> bool:
            if node is None or node.value == 0:
                return False
            # Add current node to path
            path.append(node.value)
            # If leaf, path is valid
            if node.left is None and node.right is None:
                return True
            # Traverse left subtree
            if _dfs(node.left):
                return True
            # Traverse right subtree
            if _dfs(node.right):
                return True
            # Backtrack: remove current node
            path.pop()
            return False
        if _dfs(self.root):
            return path
        else:
            return []

    def all_paths_without_zero(self) -> List[List[int]]:
        """
        Return a list of all root-to-leaf paths (each path as a list of values) where no node has value zero.
        If no such paths exist, return an empty list.
        Time Complexity: O(n), explores all nodes; space complexity O(h) for recursion stack plus result storage.
        """
        results: List[List[int]] = []
        current_path: List[int] = []
        def _dfs(node: Optional[Node]):
            if node is None or node.value == 0:
                return
            # Add current node to path
            current_path.append(node.value)
            # If leaf, record a copy of current path
            if node.left is None and node.right is None:
                results.append(current_path.copy())
            else:
                # Explore subtrees
                _dfs(node.left)
                _dfs(node.right)
            # Backtrack: remove current node
            current_path.pop()
        _dfs(self.root)
        return results







