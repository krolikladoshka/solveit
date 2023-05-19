# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [
            [0] * (len(word1) + 1)
            for _ in range(len(word2) + 1)
        ]

        for ops, i in enumerate(range(len(word2) - 1, -1, -1)):
            dp[i][len(word1)] = ops + 1

        for ops, j in enumerate(range(len(word1) - 1, -1, -1)):
            dp[len(word2)][j] = ops + 1

        for i in range(len(word2) - 1, -1, -1):
            for j in range(len(word1) - 1, -1, -1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j + 1],
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )
        return dp[0][0]
