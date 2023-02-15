# https://leetcode.com/problems/pascals-triangle
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(1, numRows):
            result.append([0] * (i + 1))
            result[i][0] = 1
            result[i][-1] = 1

            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result
