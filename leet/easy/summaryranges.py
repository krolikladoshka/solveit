# https://leetcode.com/problems/summary-ranges
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f'{nums[0]}']
        start = 0
        end = 1

        while end < len(nums):
            if (nums[end] - nums[end - 1]) > 1:
                if start == end - 1:
                    result.append(f'{nums[start]}')
                else:
                    result.append(f'{nums[start]}->{nums[end - 1]}')
                start = end
            end += 1
        if start == end - 1:
            result.append(f'{nums[start]}')
        else:
            result.append(f'{nums[start]}->{nums[end - 1]}')
        return result
