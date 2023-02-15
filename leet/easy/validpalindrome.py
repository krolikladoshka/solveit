# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            cs = s[start].lower()
            ce = s[end].lower()

            if cs != ce:
                if cs.isspace() or not cs.isalnum():
                    start += 1
                    continue
                if ce.isspace() or not ce.isalnum():
                    end -= 1
                    continue
                return False
            cs += 1
            ce += 1

        return True
