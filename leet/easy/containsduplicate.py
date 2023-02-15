# https://leetcode.com/problems/contains-duplicate/description/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for val in nums:
            s[val] = s.setdefault(val, 0) + 1
            if s[val] > 1:
                return True
        return False
