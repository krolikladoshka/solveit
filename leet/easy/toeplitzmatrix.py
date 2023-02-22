# https://leetcode.com/problems/toeplitz-matrix
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row_index, row in enumerate(matrix):
            for column_index, value in  enumerate(row):
                if row_index == 0 or column_index == 0:
                    continue
                if value != matrix[row_index - 1][column_index - 1]:
                    return False
        return True
