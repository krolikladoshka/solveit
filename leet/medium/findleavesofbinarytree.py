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
            current_height = max(left_height, right_height) + 1

            if current_height > len(result) - 1:
                result.append([])
            result[current_height].append(r.val)

            return current_height
        traverse(root)
        return result
