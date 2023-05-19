# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
from collections import deque
from typing import Optional, List

from leet.structures import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 1)])
        level_values = deque()
        result = []

        from_left_to_right = True
        prev_level = 1

        while queue:
            node, level = queue.popleft()

            if level != prev_level:
                prev_level = level
                from_left_to_right = not from_left_to_right
                result.append(list(level_values))
                level_values.clear()
            if from_left_to_right:
                level_values.append(node.val)
            else:
                level_values.appendleft(node.val)

            children = [node.left, node.right]
            for child in children:
                if not child:
                    continue
                queue.append((child, level + 1))

        result.append(list(level_values))

        return result
