# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        end1 = m - 1
        end2 = n - 1

        for i in range(m + n - 1, -1, -1):
            if end1 >= 0 and end2 >= 0:
                if nums1[end1] < nums2[end2]:
                    nums1[i] = nums2[end2]
                    end2 -= 1
                else:
                    nums1[i] = nums1[end1]
                    end1 -= 1
            elif end1 >= 0:
                nums1[i] = nums1[end1]
                end1 -= 1
            else:
                nums1[i] = nums2[end2]
                end2 -= 1
        print(nums1)

    def merge_dirty(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res = []

        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i < m:
            for k in range(i, m):
                res.append(nums1[k])
        if j < n:
            for k in range(j, n):
                res.append(nums2[k])
        for i in range(len(res)):
            nums1[i] = res[i]
