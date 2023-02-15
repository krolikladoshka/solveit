# https://leetcode.com/problems/range-sum-of-bst/
from collections import deque
from typing import Optional

from leet.structures import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        deq = deque(((root.val, root),))
        sm = 0

        while deq:
            val, node = deq.popleft()
            if low <= val <= high:
                sm += val
            if node.left:
                deq.append((node.left.val, node.left))
            if node.right:
                deq.append((node.right.val, node.right))
        return sm

