# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional

from leet.structures import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(r, mn, mx):
            if r is None:
                return True
            if mn < r.val < mx:
                return validate(r.left, mn, r.val) and validate(r.right, r.val, mx)
            return False
        return validate(root, float('-inf'), float('inf'))
