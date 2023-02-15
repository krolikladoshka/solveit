# https://leetcode.com/problems/insert-delete-getrandom-o1/
import random


class RandomizedSet:

    def __init__(self):
        self.dct = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        self.dct[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dct:
            return False
        last, idx = self.values[-1], self.dct[val]
        self.values[idx] = last
        self.dct[last] = idx
        self.values.pop()
        self.dct.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
