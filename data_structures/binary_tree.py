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

