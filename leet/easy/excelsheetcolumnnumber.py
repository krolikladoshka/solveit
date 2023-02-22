# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        base = 1
        for c in reversed(columnTitle):
            digit = (ord(c) - ord('A')) + 1
            res += base * digit
            base *= 26
        return res
