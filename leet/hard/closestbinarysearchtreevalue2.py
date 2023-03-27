# https://leetcode.com/problems/closest-binary-search-tree-value-ii

from collections import deque
from leet.structures import TreeNode
from heapq import heappop, heappush, heappushpop
from typing import Optional


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if len(heap) >= k:
                heappushpop(heap, (-abs(target - node.val), node.val))
            else:
                heappush(heap, (-abs(target - node.val), node.val))
    
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result = []
        while heap:
            result.append(heappop(heap)[1])
        
        return result
        