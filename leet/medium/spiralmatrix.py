# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_boundary = 0
        bottom_boundary = len(matrix)
        left_boundary = 0
        right_boundary = len(matrix[0])
        result = []

        while len(result) < len(matrix) * len(matrix[0]):
            for i in range(left_boundary, right_boundary):
                result.append(matrix[top_boundary][i])
            for i in range(top_boundary + 1, bottom_boundary):
                result.append(matrix[i][right_boundary - 1])

            if top_boundary != bottom_boundary - 1:
                for i in range(right_boundary - 2, left_boundary - 1, -1):
                  result.append(matrix[bottom_boundary - 1][i])
            if left_boundary != right_boundary - 1:
                for i in range(bottom_boundary - 2, top_boundary, -1):
                    result.append(matrix[i][left_boundary])

            left_boundary += 1
            right_boundary -= 1
            top_boundary += 1
            bottom_boundary -= 1

        return result
