# https://leetcode.com/problems/binary-tree-postorder-traversal/
from collections import deque
from typing import Optional, List

from leet.structures import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        deq = deque((root,))
        while deq:
            node = deq[-1]
            if node.right:
                deq.append(node.left)
            if node.left:
                deq.append(node.left)
            node = deq.pop()
            result.append(node.val)
        return result

    def postorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def walk(r):
            if not r:
                return
            if r.left:
                walk(r.left)
            if r.right:
                walk(r.right)
            result.append(r.val)

        walk(root)

        return result
