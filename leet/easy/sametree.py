# Definition for a binary tree node.

from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        def check(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val

        while stack:
            t1, t2 = stack.pop()

            if not check(t1, t2):
                return False

            if t1:
                stack.append((t1.right, t2.right))
                stack.append((t1.left, t2.left))
        return True
