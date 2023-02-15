# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, current_temperature in enumerate(temperatures):
            while stack and current_temperature > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result

    def dailyTemperatures_dirty(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        stack = [(0, temperatures[0])]
        result = [0] * len(temperatures)
        i = 1
        while i < len(temperatures):
            current_temperature = temperatures[i]
            if stack:
                index, temperature = stack[-1]
                if current_temperature > temperature:
                    stack.pop()
                    result[index] = i - index
                    continue
            stack.append((i, current_temperature))
            i += 1
        return result
