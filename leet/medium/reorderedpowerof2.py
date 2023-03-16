# https://leetcode.com/problems/reordered-power-of-2/
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers_of_two_counts = [
            Counter(str(1 << i))
            for i in range(32)
        ]

        counter = Counter(str(n))

        for power_of_two_count in powers_of_two_counts:
            if power_of_two_count == counter:
                return True
        return False
