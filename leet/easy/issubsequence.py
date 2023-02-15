# https://leetcode.com/problems/is-subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        index = 0
        for s_character in s:
            if index >= len(t):
                return False
            found = False
            while index < len(t):
                if s_character == t[index]:
                    found = True
                    index += 1
                    break
                index += 1
            if not found:
                return False
        return True
