from typing import Any, Optional


class TreeNode:
    left: Optional['TreeNode']
    right: Optional['TreeNode']
    value: Optional[Any]

    def __init__(self, value: Optional[Any], left: Optional['TreeNode'] = None, right: Optional[TreeNode] = None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    root: Optional[TreeNode]

    def __init__(self):
        self.root = None

    def insert(self, val: Any):
        if not self.root:
            self.root = TreeNode(value=val)
            return

    def rebalance(self):
        pass

    def find(self):
        pass

    def remove(self):
        pass
