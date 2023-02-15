# https://leetcode.com/problems/binary-tree-maximum-path-sum
from typing import Optional

from leet.structures import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def find_max_sum(r, max_sum):
            if not r:
                return 0

            left_sum = max(find_max_sum(r.left, max_sum), 0)
            right_sum = max(find_max_sum(r.right, max_sum), 0)

            max_sum = max(max_sum, left_sum + right_sum + r.val)

            return max(left_sum + r.val, right_sum + r.val, max_sum)


        return find_max_sum(root, float('-inf'))
