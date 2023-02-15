# https://leetcode.com/problems/text-justification/
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        pass

    def justify_words(self, words: List[str], maxWidth: int):
        spaces = maxWidth
        evenly = (maxWidth // len(words)) - 1
        left = (maxWidth % len(words))
        res = []
        i = 0
        while spaces > 0:
            res.append(words[i])
            res.append(evenly)
            left -= (len(words[i]) + evenly)
            i += 1