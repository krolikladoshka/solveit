# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)

        for i in range(len(nums) -1, -1 , -1):
            if abs(nums[left]) < abs(nums[right]):
                res[i] = nums[right] * nums[right]
                right -= 1
            else:
                res[i] = nums[left] * nums[left]
                left += 1
        return res
