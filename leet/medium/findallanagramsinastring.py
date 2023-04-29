# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import defaultdict
from typing import List


class Solution:
    def counter(self, s):
        counter = {}

        for c in s:
            counter[c] = counter.setdefault(c, 0) + 1
        return counter

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_counter = self.counter(p)

        window = len(p)

        i = 0
        result = []
        counter = defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1

            if i >= window:
                if counter[s[i - window]] == 1:
                    counter.pop(s[i - window])
                else:
                    counter[s[i - window]] -= 1

            if p_counter == counter:
                result.append(i - window + 1)
        return result
