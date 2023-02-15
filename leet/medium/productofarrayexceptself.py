# https://leetcode.com/problems/product-of-array-except-self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

    def productExceptSelf_nspace(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * (len(nums) + 1)
        suffix_product = [1] * (len(nums) + 1)
        i, j = 0, len(nums) - 1
        prefix, suffix = 1, 1
        while i < len(nums):
            prefix *= nums[i]
            suffix *= nums[j]
            prefix_product[i + 1] = prefix
            suffix_product[j] = suffix
            i += 1
            j -= 1

        res = []
        for i in range(0, len(prefix_product) - 1):
            res.append(prefix_product[i] * suffix_product[i + 1])

        return res