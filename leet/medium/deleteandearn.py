# https://leetcode.com/problems/delete-and-earn
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counted = {}
        cache = {}
        max_num = -1
        for num in nums:
            if num > max_num:
                max_num = num
            counted[num] = counted.setdefault(num, 0) + num

        def calculate(num):
            if num == 1:
                return counted.get(1, 0)
            if num == 0:
                return 0

            if num in cache:
                return cache[num]
            cache[num] = max(calculate(num - 1), calculate(num - 2) + (counted.get(num, 0)))
            return cache[num]

        return calculate(max_num)

