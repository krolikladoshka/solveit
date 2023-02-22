# https://leetcode.com/problems/binary-tree-preorder-traversal
from collections import deque
from typing import Optional, List

from leet.structures import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [(root, root.val)]

        while stack:
            node, val = stack.pop()
            result.append(val)

            if node.right:
                stack.append((node.right, node.right.val))
            if node.left:
                stack.append((node.left, node.left.val))
        return result

    def preorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def walk(r):
            if not r:
                return
            result.append(r.val)
            print(result)

            if r.left:
                walk(r.left)
            if r.right:
                walk(r.right)

        walk(root)

        return result
