# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        prefix_sum = 0
        counter = 0

        for value in nums:
            prefix_sum += value
            seen = prefix_sums.get(prefix_sum - k, 0)
            counter += seen
            prefix_sums[prefix_sum] = prefix_sums.setdefault(prefix_sum, 0) + 1

        return counter
