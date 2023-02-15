# https://leetcode.com/problems/first-missing-positive
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            j = nums[i] - 1

            if (j >= 0 and j < n) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

    def firstMissingPositive_leet(self, nums: List[int]) -> int:
        if not 1 in nums:
            return 1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            x = abs(nums[i])

            if x == n:
                nums[0] = -abs(nums[0])
            else:
                nums[x] = -abs(nums[x])

        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1
