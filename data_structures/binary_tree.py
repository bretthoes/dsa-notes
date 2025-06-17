class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = TreeNode(value)

"""
Binary Search Tree (BST)
A binary tree that has a certain sorted property in the ordering of tree nodes.
Every left node will have a value LESS than it's parent, and every right node will have a value greater than it's parent.
"""
class BinarySearchTree:
    def __init__(self, value):
        self.root = TreeNode(value)

    def search(self, target):
        """
        O(log n)
        """
        def search(root, target) -> TreeNode | None:
            if not root:
                return None

            if root.value > target:
                search(root.left, target)
            elif root.value < target:
                search(root.right, target)
            else:
                return root

        return search(self.root, target)

    def insert(self, value):
        """
        O(log n)
        """
        def insert(root, value):
            if not root:
                return TreeNode(value)
            if value < root.value:
                root.left = insert(root.left, value)
            else:
                root.right = insert(root.right, value)
            return root
        return insert(self.root, value)

    def getMin(self):
        """
        O(log n)
        """
        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur

    def remove(self, value):
        """
        Case 1:
            Node to remove has 0 or 1 child
        Case 2:
            Node to remove has 2 children. In this case, need to replace node with either:
            - Largest value in right subtree, or
            - Smallest value in left subtree
        """
        def remove(root: TreeNode | None, value: int):
            if not root:
                return
            if value < root.value:
                root.left = remove(root.left, value)
            elif value > root.value:
                root.right = remove(root.right, value)
            else: # remove this node
                if not root.left and not root.right: # 0 children
                    return None
                elif root.left and not root.right: # 1 child
                    return root.left
                elif root.right and not root.left: # 1 child
                    return root.right
                else: # 2 children
                    # TODO handle 2 children
                    return None

        remove(self.root, value)



















