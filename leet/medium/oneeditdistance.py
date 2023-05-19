# https://leetcode.com/problems/one-edit-distance/
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        i, j = 0, 0

        while i < len(s):
            if s[i] != t[j]:
                if len(s) == len(t):
                    return s[i + 1:] == t[j + 1:]
                return s[i:] == t[j + 1:]

            i += 1
            j += 1
        if s == t == '':
            return False
        return len(s) != len(t)
