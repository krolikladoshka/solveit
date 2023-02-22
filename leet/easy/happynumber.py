# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        not_happy_loops = {4, 16, 37, 58, 89, 145, 42, 20, 4}

        def squares_of_digits(value):
            res = 0
            while value > 0:
                res += (value % 10) ** 2
                value //= 10
            return res

        while True:
            if n in not_happy_loops:
                return False
            if n in {1, 7}:
                return True
            n = squares_of_digits(n)
