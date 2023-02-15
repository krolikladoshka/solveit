# https://leetcode.com/problems/running-sum-of-1d-array
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = 0
        result = []
        for i in range(len(nums)):
            prefix += nums[i]
            result.append(prefix)
        return result
