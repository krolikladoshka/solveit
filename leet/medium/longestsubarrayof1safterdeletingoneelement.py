# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        zeroes_in_window = 0
        max_length = 0

        while right < len(nums):
            # if right == left and nums[right] == 0:
            #     zeroes_in_window += 1
            #     right += 1
            #     continue
            if nums[right] == 1:
                right += 1
                max_length = max(max_length, right - left - 1)
            else:
                zeroes_in_window += 1
                if zeroes_in_window > 1:
                    if nums[left] == 1:
                        while nums[left] != 0:
                            left += 1
                        left += 1
                        zeroes_in_window -= 1
                    else:
                        left += 1
                else:
                    max_length = max(max_length, right - left)

                right += 1
        return max_length
