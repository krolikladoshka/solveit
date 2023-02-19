# https://leetcode.com/problems/minimum-depth-of-binary-tree
from typing import Optional

from leet.structures import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def find_minimum_depth(r):
            if not r:
                return 0
            if not r.left:
                return find_minimum_depth(r.right) + 1
            elif not r.right:
                return find_minimum_depth(r.left) + 1
            return 1 + min(find_minimum_depth(r.right), find_minimum_depth(r.left))

        return find_minimum_depth(root)
