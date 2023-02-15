# https://leetcode.com/problems/combinations/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(first, combinations):
            if len(combinations) == k:
                yield [c for c in combinations]
            for i in range(first, n + 1):
                combinations.append(i)
                yield from solve(i + 1, combinations)
                combinations.pop()

        return list(solve(1, []))
