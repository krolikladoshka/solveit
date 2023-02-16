# https://leetcode.com/problems/substring-xor-queries
from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        substrings = {}

        for i in range(len(s)):
            bin_value = 0

            for j in range(i, min(i + 32, len(s))):
                bin_value = bin_value * 2 + int(s[j])

                if bin_value not in substrings:
                    substrings[bin_value] = [i, j]
                if bin_value == 0:
                    break

        queries_result = []
        for query in queries:
            operand, result = query

            substring = result ^ operand
            queries_result.append(substrings.get(substring, [-1, -1]))

        return queries_result
