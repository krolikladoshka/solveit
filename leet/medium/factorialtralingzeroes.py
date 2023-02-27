# https://leetcode.com/problems/factorial-trailing-zeroes
class Solution:
    def trailingZeroes(self, n: int) -> int:
        counter = 0
        while n >= 5:
            n //= 5
            counter += n
        return counter
