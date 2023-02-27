# https://leetcode.com/problems/sort-colors
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for num in nums:
            colors[num] += 1

        idx = 0
        for color, count in enumerate(colors):
            for i in range(count):
                nums[idx] = color
                idx += 1
