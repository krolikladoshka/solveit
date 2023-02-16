from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def count_lower(value):
            i = 0
            j = len(nums) - 1
            counter = 0

            while i < j:
                if nums[i] + nums[j] <= value:
                    counter += j - i
                    i += 1
                else:
                    j -= 1
            return counter
        return abs(count_lower(upper) - count_lower(lower - 1))
