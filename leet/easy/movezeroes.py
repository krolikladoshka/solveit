# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift_to_left = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                shift_to_left += 1
            else:
                nums[i - shift_to_left], nums[i] = nums[i], nums[i - shift_to_left]
