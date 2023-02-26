# https://leetcode.com/problems/slowest-key/
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]
        prev_duration = releaseTimes[0]
        max_duration_index = 0

        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - prev_duration

            if duration > max_duration or (
                    duration == max_duration
                    and keysPressed[i] >= keysPressed[max_duration_index]
            ):
                max_duration_index = i
                max_duration = duration
            prev_duration = releaseTimes[i]

        return keysPressed[max_duration_index]
