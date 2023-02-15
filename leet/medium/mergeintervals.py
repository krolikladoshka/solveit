# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        result = []
        intervals.sort(key=lambda x: x[0])

        def overlap(a, b):
            s1, e1 = a
            s2, e2 = b

            return s1 <= e2 and s2 <= e1

        current_interval = intervals[0]
        i = 1
        while i < len(intervals):
            if overlap(current_interval, intervals[i]):
                current_interval[0] = min(current_interval[0], intervals[i][0])
                current_interval[1] = max(current_interval[1], intervals[i][1])
                i += 1
            else:
                result.append(current_interval)
                current_interval = intervals[i]
        result.append(current_interval)

        return result