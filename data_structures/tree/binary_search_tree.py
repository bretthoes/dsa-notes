from binary_tree import TreeNode

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
        O(log n) average, O(n) worst-case.
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
        O(log n) average, O(n) worst-case.
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

    def getMin(self, cur):
        """
        O(log n) average, O(n) worst-case.
        """
        while cur and cur.left:
            cur = cur.left
        return cur

    def remove(self, value):
        """
        Remove `value` from the BST.
        Case 1: Node has 0 or 1 child.
        Case 2: Node has 2 children: replace with in-order successor.
        """
        def _remove(root: TreeNode | None, value: int):
            if not root:
                return None

            if value < root.value:
                root.left = _remove(root.left, value)
            elif value > root.value:
                root.right = _remove(root.right, value)
            else:
                # --- Case 1: zero or one child ---
                if root.left is None and root.right is None:
                    return None
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left

                # --- Case 2: two children ---
                # 1. Find successor (smallest in right subtree)
                succ = self.getMin(root.right)
                # 2. Copy its value
                root.value = succ.value
                #. 3. Delete successor
                root.right = _remove(root.right, succ.value)

            return root
                
        self.root = _remove(self.root, value)


    def ascending(self):
        """
        DFS
        """
        def _inOrder(root: TreeNode | None):
            if not root:
                return
            _inOrder(root.left)
            print(root.value)
            _inOrder(root.right)

        _inOrder(self.root)
 
    def descending(self):
        """
        DFS
        """
        def _descending(root: TreeNode | None):
            if not root:
                return
            _descending(root.right)
            print(root.value)
            _descending(root.left)

        _descending(self.root)

    def preOrder(self):
        """
        DFS
        """
        def _preOrder(root: TreeNode | None):
            if not root:
                return
            print(root.value)
            _preOrder(root.left)
            _preOrder(root.right)

        _preOrder(self.root)

    def print(self, node):
        print(node.value)

    def bfs(self):
        queue = deque()
        if self.root:
            queue.append(self.root)

        level = 0
        while queue:
            print("level: ", level)
            for _ in range(len(queue)):
                node = queue.popleft()
                print(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1


















