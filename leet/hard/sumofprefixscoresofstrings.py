# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_counter = {}

        for word in words:
            # prefix_counter[word] = 1
            for end in range(len(word), 0, -1):
                prefix = word[:end]
                prefix_counter[prefix] = prefix_counter.setdefault(prefix, 0) + 1

        result = []
        for i, word in enumerate(words):
            result.append(0)
            for end in range(len(word), 0, -1):
                prefix = word[:end]
                result[i] += prefix_counter[prefix]
        return result
