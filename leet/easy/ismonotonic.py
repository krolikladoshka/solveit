# https://leetcode.com/problems/monotonic-array/
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        for i in range(len(nums) - 1):
            if nums[0] < nums[-1]:
                if nums[i] > nums[i + 1]:
                    return False
            elif nums[0] > nums[-1]:
                if nums[i] < nums[i + 1]:
                    return False
            else:
                if nums[i] != nums[i + 1]:
                    return False
        return True
