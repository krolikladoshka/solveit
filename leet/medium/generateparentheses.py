# https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, parentheses):
            if len(parentheses) == n * 2:
                yield parentheses
            if left < n:
                parentheses += '('
                yield from backtrack(left + 1, right, parentheses)
                parentheses = parentheses[:len(parentheses) - 1]
            if right < left:
                parentheses += ')'
                yield from backtrack(left, right + 1, parentheses)
        return list(backtrack(0, 0, ''))

