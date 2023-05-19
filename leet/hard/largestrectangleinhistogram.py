# https://leetcode.com/problems/largest-rectangle-in-histogram
from itertools import chain
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(chain([0], heights, [0])):
            while stack and stack[-1][1] > height:
                _, candidate_height = stack.pop()
                left_boundary = stack[-1][0] + 1

                max_area = max(
                    max_area,
                    candidate_height * (i - left_boundary)
                )
            stack.append((i, height))
        return max_area

    def largestRectangleArea1(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area

