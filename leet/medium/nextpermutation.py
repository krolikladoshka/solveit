# https://leetcode.com/problems/next-permutation/
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_decreasing = -1
        index = len(nums) - 1
        while index > 0:
            if nums[index - 1] < nums[index]:
                first_decreasing = index - 1
                break
            index -= 1

        if first_decreasing >= 0:
            swap_place = len(nums) - 1
            index = len(nums) - 1
            while index > first_decreasing:
                if nums[index] > nums[first_decreasing]:
                    swap_place = index
                    break
                index -= 1
            nums[first_decreasing], nums[swap_place] = nums[swap_place], nums[first_decreasing]

        start = first_decreasing + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
