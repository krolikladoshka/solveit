# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                start = i + 1
                end = len(nums) - 1

                while start < end:
                    sm = nums[i] + nums[start] + nums[end]
                    if sm < 0:
                        start += 1
                    elif sm > 0:
                        end -= 1
                    else:
                        res.append([nums[i], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
        return res
