# https://leetcode.com/problems/palindrome-number/
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False

        reversed_second_half = 0
        while x > reversed_second_half:
            reversed_second_half = reversed_second_half * 10 + x % 10
            x //= 10

        return reversed_second_half == x or x == reversed_second_half // 10

    def isPalindrome_linear(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        x = abs(x)
        digits_count = int(math.log10(x) + 1)

        while x != 0:
            base = 10 ** (digits_count - 1)
            first = x // base
            last = x % 10

            if first != last:
                return False
            x -= first * base
            x //= 10
            digits_count -= 2

        return True
