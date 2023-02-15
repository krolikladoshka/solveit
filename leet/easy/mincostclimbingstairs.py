# https://leetcode.com/problems/min-cost-climbing-stairs
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        dp[len(cost)] = min(dp[len(cost) - 1], dp[len(cost) - 2])

        return dp[-1]
