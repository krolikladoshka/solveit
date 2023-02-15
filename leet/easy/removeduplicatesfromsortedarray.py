# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        highest = nums[0]
        unique_count = 1
        duplicates_count = 0

        for i in range(1, len(nums)):
            if nums[i] == highest:
                duplicates_count += 1
            else:
                unique_count += 1
                highest = nums[i]
                nums[i], nums[i - duplicates_count] = nums[i - duplicates_count], nums[i]

        return unique_count