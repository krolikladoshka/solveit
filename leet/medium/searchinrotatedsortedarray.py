# https://leetcode.com/problems/search-in-rotated-sorted-array-ii
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target or nums[start] == target or nums[end] == target:
                return True
            elif nums[mid] < target < nums[end]:
                start = mid + 1
            elif nums[start] < target < nums[mid]:
                end = mid - 1
            else:
                start += 1
                end -= 1
        return False
