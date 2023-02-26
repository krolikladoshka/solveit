# https://leetcode.com/problems/flatten-binary-tree-to-linked-list
from collections import deque
from typing import Optional

from leet.structures import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        deq = deque([root])
        pre_head = TreeNode(val=-1)
        walk = pre_head
        while deq:
            node = deq.pop()

            if node:
                if node.right:
                    deq.append(node.right)
                if node.left:
                    deq.append(node.left)
                walk.right = node
                walk.left = None
                walk = walk.right
        pre_head.right = None
