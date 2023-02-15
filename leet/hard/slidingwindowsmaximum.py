# https://leetcode.com/problems/sliding-window-maximum
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not len(nums) or not k:
            return []
        if k == 1:
            return nums

        deq = deque()
        result = []

        def clean_deque(idx):
            if deq and deq[0] == idx - k:
                deq.popleft()

            while deq and nums[deq[-1]] < nums[idx]:
                deq.pop()
        for i in range(k):
            clean_deque(i)
            deq.append(i)
        result.append(nums[deq[0]])

        for i in range(k, len(nums)):
            clean_deque(i)
            deq.append(i)
            result.append(nums[deq[0]])

        return result
