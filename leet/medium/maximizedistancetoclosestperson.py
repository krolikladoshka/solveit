from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        running_max_left = [len(seats)] * len(seats)

        i = 0
        while i < len(seats):
            if seats[i] == 1:
                running_max_left[i] = 0
            elif i > 0:
                running_max_left[i] = running_max_left[i - 1] + 1
            i += 1

        running_max_right = [len(seats)] * len(seats)
        i = len(seats) - 1
        while i >= 0:
            if seats[i] == 1:
                running_max_right[i] = 0
            elif i < len(seats) - 1:
                running_max_right[i] = running_max_right[i + 1] + 1
            i -= 1

        max_distance = max(
            map(min, zip(running_max_left, running_max_right))
        )

        return max_distance
