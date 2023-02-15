# https://leetcode.com/problems/find-pivot-index
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tsum = 0
        for val in nums:
            tsum += val
        prefix_sum = 0
        for i, val in enumerate(nums):
            if prefix_sum == tsum - prefix_sum - val:
                return i
            prefix_sum += val
        return -1
