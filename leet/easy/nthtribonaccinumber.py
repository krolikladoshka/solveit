# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def calculate(k):
            if k == 0:
                return 0
            if k < 3:
                return 1
            if k in memo:
                return memo[k]
            memo[k] = calculate(k - 3) + calculate(k - 2) + calculate(k - 1)

            return memo[k]

        return calculate(n)
