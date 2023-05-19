# https://leetcode.com/problems/maximal-rectangle/
from itertools import chain
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def get_largest_rectangle(histogram: List[int]) -> int:
            max_rectangle = 0
            stack = []

            for i, height in enumerate(chain([0], histogram, [0])):
                while stack and stack[-1][1] > height:
                    _, right_boundary_height = stack.pop()
                    left_boundary = stack[-1][0] + 1
                    rectangle_width = i - left_boundary

                    max_rectangle = max(
                        max_rectangle,
                        right_boundary_height * rectangle_width
                    )
                stack.append((i, height))

            return max_rectangle

        max_rectangle = 0
        histogram = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    histogram[j] += 1
                else:
                    histogram[j] = 0

            largest_rectangle = get_largest_rectangle(histogram)
            max_rectangle = max(max_rectangle, largest_rectangle)
        return max_rectangle
