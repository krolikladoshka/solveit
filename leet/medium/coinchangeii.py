# https://leetcode.com/problems/coin-change-ii
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]

    def change1(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for coin_index, coin in enumerate(coins, start=1):
            for i in range(amount + 1):
                if i < coin:
                    dp[coin_index][i] = dp[coin_index - 1][i]
                else:
                    dp[coin_index][i] = dp[coin_index - 1][i] + dp[coin_index][i - coin]

        return dp[len(coins)][amount]