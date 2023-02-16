from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sorter(point):
            return point[0] * point[0] + point[1] * point[1]
        return sorted(points, key=sorter)[:k]