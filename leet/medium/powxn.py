# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if x == 1:
            return x
        if n < 0:
            x = 1 / x
            n = -n

        def pw(v, k):
            if k == 0:
                return 1
            if k == 1:
                return v

            if k % 2 == 1:
                pow = pw(v, (k - 1) // 2)
                return v * pow * pow
            else:
                pow = pw(v, k // 2)
                return pow * pow

        return pw(x, n)
