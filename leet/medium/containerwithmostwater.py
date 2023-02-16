# https://leetcode.com/problems/container-with-most-water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            if area > max_area:
                max_area = area
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_area
