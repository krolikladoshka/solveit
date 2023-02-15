# https://leetcode.com/problems/symmetric-tree

from typing import Optional

from leet.structures import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        if not root.left and root.right:
            return False
        if not root.right and root.left:
            return False
        return self.helper(root.left, root.right)

    def helper(self, t1, t2) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.helper(t1.left, t2.right) and self.helper(t1.right, t2.left)
