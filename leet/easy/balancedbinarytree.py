# https://leetcode.com/problems/balanced-binary-tree
from typing import Optional

from leet.structures import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]

    def helper(self, tree):
        if not tree:
            return True, 0

        left_balanced, left_height = self.helper(tree.left)
        if not left_balanced:
            return False, left_height
        right_balanced, right_height = self.helper(tree.right)
        if not right_balanced:
            return False, right_height

        return abs(left_height - right_height) <= 1, 1 + max(left_height, right_height)

    def isBalanced_topdown(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.helper_1(root.left) - self.helper_1(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def helper_1(self, tree) -> bool:
        if not tree:
            return 0
        return 1 + max(self.helper_1(tree.left), self.helper_1(tree.right))
