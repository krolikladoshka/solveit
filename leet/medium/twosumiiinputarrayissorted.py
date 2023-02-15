from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            sm = numbers[start] + numbers[end]
            if sm < target:
                start += 1
            elif sm > target:
                end -= 1
            else:
                return [start + 1, end + 1]
