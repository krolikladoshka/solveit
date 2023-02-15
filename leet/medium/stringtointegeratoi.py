# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        def skip(i, chars):
            while i < len(s) and s[i] in chars:
                i += 1
            return i
        index = skip(0, {' ', '\n', '\r'})
        if index >= len(s):
            return 0
        sign = 1
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            sign = 1
            index += 1

        digits = []
        index = skip(index, '0')
        if index > len(s):
            return 0

        while index < len(s) and s[index].isdigit():
            digits.append(int(s[index]))
            index += 1

        res = 0
        base = 1
        for i in range(len(digits) - 1, -1, -1):
            rs = res + base * digits[i]
            if rs > (2 ** 31 - 1):
                return sign * (2 ** 31 - (1 if sign > 0 else 0))
            res = rs
            base *= 10

        return sign * res
