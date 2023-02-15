# https://leetcode.com/problems/find-leaves-of-binary-tree/
from typing import Optional, List

from leet.structures import TreeNode


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def traverse(r):
            if not r:
                return -1
            left_height = traverse(r.left)
            right_height = traverse(r.right)
            height = max(left_height, right_height) + 1

            if height >= len(result):
                result.append([])
            result[height].append(r.val)

            return height

        traverse(root)

        return result
