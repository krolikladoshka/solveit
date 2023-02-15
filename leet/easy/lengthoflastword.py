# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        ln = 0
        while i >= 0 and s[i] != ' ':
            ln += 1
            i -= 1

        return ln

    def lengthOfLastWord_index(self, s: str) -> int:
        i = len(s) - 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                break
        return i - s.rfind(' ', 0, i + 1)
