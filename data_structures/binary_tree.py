from typing import Optional, List


class TreeNode:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, value: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """
    Represents a binary tree with utility methods for path-finding.
    """
    def __init__(self, root: Optional[TreeNode] = None):
        """
        Initialize the binary tree.

        :param root: Optional root TreeNode. If None, tree is empty.
        """
        self.root = root

    def has_path_without_zero(self) -> bool:
        """
        Determine if there exists at least one root-to-leaf path with no node values equal to zero.

        :return: True if such a path exists, False otherwise.
        Time Complexity: O(n), where n is the number of nodes.
        """
        def _dfs(node: Optional[TreeNode]) -> bool:
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

        def _dfs(node: Optional[TreeNode]) -> bool:
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

        def _dfs(node: Optional[TreeNode]):
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


if __name__ == "__main__":
    # Example usage:
    # Build a sample tree:
    #       1
    #      / \
    #     2   5
    #    / \   \
    #   3   4   0
    # Paths without zero: [1,2,3] and [1,2,4]
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(0)
    )
    tree = BinaryTree(root)
    print("Has path without zero:", tree.has_path_without_zero())  # Expected: True
    print("First path without zero:", tree.first_path_without_zero())  # Expected: [1, 2, 3]
    print("All paths without zero:", tree.all_paths_without_zero())  # Expected: [[1, 2, 3], [1, 2, 4]]
