# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for c in t:
            d[c] = d.setdefault(c, 0) + 1
        for c in s:
            d[c] = d.setdefault(c, 0) + 1

        for c, count in d.items():
            if count % 2 != 0:
                return c
