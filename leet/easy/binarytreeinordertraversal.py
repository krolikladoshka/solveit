# https://leetcode.com/problems/binary-tree-inorder-traversal
from typing import Optional, List

from leet.structures import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(r: Optional[TreeNode]):
            if not r:
                return
            if r.left:
                traverse(r.left)
            result.append(r.val)

            if r.right:
                traverse(r.right)

        traverse(root)

        return result
