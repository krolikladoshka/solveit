from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        counter = 0
        jump = 0
        last_position = 0
        i = 0
        while i < len(nums) - 1:
            jump = max(i + nums[i], jump)
            if i == last_position:
                last_position = jump
                counter += 1
            i += 1

        return counter
