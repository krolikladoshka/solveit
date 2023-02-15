# https://leetcode.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = -1
        max_height_idx = -1
        for i, h in enumerate(height):
            if h > max_height:
                max_height = h
                max_height_idx = i

        result = 0
        left_hill = -1
        for i in range(max_height_idx):
            if left_hill < height[i]:
                left_hill = height[i]
            else:
                result += left_hill - height[i]
        right_hill = -1
        for i in range(len(height) - 1, max_height_idx, -1):
            if right_hill < height[i]:
                right_hill = height[i]
            else:
                result += right_hill - height[i]
        return result
