# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional

from leet.structures import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        stack = [(root, 1)]

        while stack:
            root, current_level = stack.pop()

            if root:
                level = max(current_level, level)
                stack.append((root.left, current_level + 1))
                stack.append((root.right, current_level + 1))
        return level

    def maxDepth_dirty(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        return self.helper(root, 0)

    def helper(self, tree, level) -> int:
        if not tree:
            return level
        level += 1
        left_level, right_level = level, level
        if tree.left:
            left_level = max(self.helper(tree.left, level), level)
        if tree.right:
            right_level = max(self.helper(tree.right, level), level)

        return max(left_level, right_level)