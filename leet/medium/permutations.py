# https://leetcode.com/problems/permutations/description/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(idx):
            if idx == len(nums):
                yield nums[:]
                return
            for i in range(idx, len(nums)):
                print(nums[:], 'before swapped')
                nums[i], nums[idx] = nums[idx], nums[i]
                print(nums[:], 'swapped')
                yield from solve(idx + 1)
                print(nums[:], 'before_restored')
                nums[i], nums[idx] = nums[idx], nums[i]
                print(nums[:], 'restored')
        return list(solve(0))
