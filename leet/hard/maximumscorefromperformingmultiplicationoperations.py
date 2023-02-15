# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations
from typing import List


class Solution:
    def maximumScore_topdown(self, nums: List[int], multipliers: List[int]) -> int:
        cache = {}

        def calculate(left, multiplier_idx):
            if multiplier_idx == len(multipliers):
                return 0

            if (left, multiplier_idx) in cache:
                return cache[(left, multiplier_idx)]

            pick_left = nums[left] * multipliers[multiplier_idx] + calculate(
                left + 1, multiplier_idx + 1
            )
            pick_right = nums[len(nums) - 1 - (multiplier_idx - left)] * multipliers[multiplier_idx] + calculate(
                left, multiplier_idx + 1
            )

            result = max(pick_right, pick_left)
            cache[(left, multiplier_idx)] = result
            return result
        return calculate(0, 0)
