from typing import Optional

from leet.structures import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.left_inorder(root)

    def left_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()

        if node.right:
            self.left_inorder(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

