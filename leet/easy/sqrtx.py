# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        start = 2
        end = x // 2

        while start <= end:
            mid = (end + start) // 2

            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid + 1
            else:
                return mid
        return end
