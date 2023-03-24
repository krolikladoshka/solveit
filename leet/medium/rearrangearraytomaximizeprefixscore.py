# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        score = 0
        nums = sorted(nums, reverse=True)
        if nums[0] <= 0:
            return 0
        for i, val in enumerate(nums):
            score += val
            if score <= 0:
                return i
        return len(nums)
