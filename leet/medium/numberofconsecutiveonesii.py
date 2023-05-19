# https://leetcode.com/problems/max-consecutive-ones-ii
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        num_of_zeroes = 0
        longest_sequence = 0

        for i, val in enumerate(nums):
            if val == 0:
                num_of_zeroes += 1
            if num_of_zeroes <= 1:
                longest_sequence = max(
                    longest_sequence,
                    i - left + 1
                )
            else:
                while num_of_zeroes > 1:
                    if nums[left] == 0:
                        num_of_zeroes -= 1
                    left += 1

        return longest_sequence
