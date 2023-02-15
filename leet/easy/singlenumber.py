# https://leetcode.com/problems/single-number
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        value = 0
        for val in nums:
            value ^= val
        return value
