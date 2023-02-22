from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1_index = nums2_index = 0
        m = len(nums1)
        n = len(nums2)
        result = []
        while nums1_index < len(nums1) or nums2_index < len(nums2):
            if nums1_index < m and nums2_index < n:
                nums1_elem = nums1[nums1_index]
                nums2_elem = nums2[nums2_index]

                if nums1_elem[0] == nums2_elem[0]:
                    result.append(
                        [nums1_elem[0], nums1_elem[1] + nums2_elem[1]]
                    )
                    nums1_index += 1
                    nums2_index += 1
                elif nums1_elem[0] < nums2_elem[0]:
                    result.append(nums1_elem)
                    nums1_index += 1
                else:
                    result.append(nums2_elem)
                    nums2_index += 1
            elif nums1_index < m:
                result.append(nums1[nums1_index])
                nums1_index += 1
            else:
                result.append(nums2[nums2_index])
                nums2_index += 1
        return result
