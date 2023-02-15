# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (end + start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return start

    def searchInsert_dirty(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        start = 0
        end = len(nums)

        while start <= end:
            mid = (end - start) // 2 + start
            if end - start == 1:
                if nums[mid] < target:
                    return end
                elif nums[mid] > target:
                    return start
                else:
                    return mid
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid
            else:
                return mid

