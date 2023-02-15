# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        cheapest = prices[0]
        i = 1
        while i < len(prices):
            if prices[i] < cheapest:
                cheapest = prices[i]
            elif prices[i] > cheapest:
                max_profit = max(prices[i] - cheapest, max_profit)
            i += 1
        return max_profit
