# https://leetcode.com/problems/path-sum/
from typing import Optional

from leet.structures import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum - root.val)]

        while stack:
            node, current_sum = stack.pop()

            if not node.left and not node.right and current_sum == 0:
                return True
            if node.right:
                stack.append((node.right, current_sum - node.left.val))
            if node.left:
                stack.append((node.left, current_sum - node.right.val))
        return False

    def hasPathSum_recursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def calculate(r, sm):
            if not r:
                return False

            sm -= r.val

            if not r.left and not r.right:
                return sm == 0
            return calculate(r.left, sm) or calculate(r.right, sm)

        return calculate(root, targetSum)
