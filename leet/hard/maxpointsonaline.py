# https://leetcode.com/problems/max-points-on-a-line/

from math import atan2
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = -1
        for i in range(len(points)):
            check_point = points[i]
            counter = {}
            for j in range(len(points)):
                if i != j:
                    vector = (
                        points[j][0] - check_point[0],
                        points[j][1] - check_point[1]
                    )
                    slope = atan2(vector[1], vector[0])
                    counter[slope] = counter.setdefault(slope, 0) + 1
            max_points = max(counter.values()) if counter.values() else 0
            result = max(result, max_points + 1)
        return result
