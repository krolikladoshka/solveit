# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, left=True)
        if left < 0:
            return [left, left]
        right = self.binary_search(nums, target, left=False)

        return [left, right]

    def binary_search(self, nums: List[int], target: int, left: bool = True) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (end + start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                if left:
                    if mid == start or nums[mid - 1] < target:
                        return mid
                    end = mid - 1
                else:
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    start = mid + 1
        return -1
