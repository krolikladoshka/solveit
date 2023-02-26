# https://leetcode.com/problems/moving-average-from-data-stream
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.current_size = 0
        self.sm = 0
        self.previous = 0
        self.previous_elements = deque()

    def next(self, val: int) -> float:
        self.sm += val - self.previous
        self.previous_elements.append(val)
        self.current_size += 1
        size = self.current_size

        if size >= self.size:
            self.current_size = self.size
            size = self.size
            self.previous = self.previous_elements.popleft()
        return self.sm / size

