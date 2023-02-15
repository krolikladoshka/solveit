# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        saved_paths = {}

        def solve(x, y) -> int:
            if x == 0 or y == 0:
                return 0
            if x == 1 and y == 1:
                return 1
            if (x, y) in saved_paths:
                return saved_paths[(x, y)]
            saved_paths[(x, y)] = solve(x - 1, y) + solve(x, y - 1)
            return saved_paths[(x, y)]

        return solve(m, n)
