# https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid_start = 0
        valid_end = len(s) - 1

        for i in range(len(s)):
            if s[i] == ')':
                valid_start += 1
            else:
                break
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                valid_end -= 1
            else:
                break

        lefts, rights = 0, 0
        max_length = 0

        for i in range(valid_start, len(s)):
            if s[i] == '(':
                lefts += 1
            else:
                rights += 1

            if lefts == rights:
                max_length = max(max_length, lefts * 2)
            elif lefts < rights:
                lefts = rights = 0

        print(valid_start, valid_end, max_length)

        lefts = rights = 0
        for i in range(valid_end, -1, -1):
            if s[i] == '(':
                lefts += 1
            else:
                rights += 1

            if lefts == rights:
                max_length = max(max_length, rights * 2)
            elif lefts > rights:
                lefts = rights = 0

        return max_length
