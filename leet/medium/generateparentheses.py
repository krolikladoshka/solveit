# https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(lefts, rights, parentheses):
            if len(parentheses) == n * 2:
                yield parentheses[:]

                return
            if lefts < n:
                parentheses.append('(')
                yield from generate(lefts + 1, rights, parentheses)
                parentheses.pop()

            if rights < lefts:
                parentheses.append(')')
                yield from generate(lefts, rights + 1, parentheses)
                parentheses.pop()

        return list(generate(0, 0, []))
