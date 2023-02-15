# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional

from leet.structures import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(val=nums[0])

        mid = len(nums) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:len(nums)])

        return root
