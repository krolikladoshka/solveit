# https://leetcode.com/problems/group-anagrams/description/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            counter = [0] * 26

            for c in s:
                counter[ord(c) - ord('a')] += 1

            counter = tuple(counter)
            result.setdefault(counter, []).append(s)

        return list(result.values())
