# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        i = 0
        while i < len(prices):
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            cheapest = prices[i]

            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            max_profit += (prices[i] - cheapest)
            i += 1
        return max_profit
