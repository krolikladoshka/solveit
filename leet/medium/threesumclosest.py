# https://leetcode.com/problems/3sum-closest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        difference = float('-inf')

        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                sm = nums[i] + nums[start] + nums[end]
                current_difference = target - sm

                if abs(current_difference) < abs(difference):
                    difference = current_difference
                if sm < target:
                    start += 1
                elif sm > target:
                    end -= 1
                else:
                    return sm
        return target - difference
