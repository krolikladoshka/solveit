# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends
from typing import List


class DisjointSet:
    def __init__(self, n: int):
        self.size = n
        self.components = n
        self.parents = [i for i in range(n)]
        self.heights = [1 for i in range(n)]

    def find(self, node: int) -> int:
        root = node
        while root != self.parents[root]:
            root = self.parents[root]

        while node != root:
            old_root = self.parents[node]
            self.parents[node] = root
            node = old_root

        return root

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.heights[root_a] > self.heights[root_b]:
            self.parents[root_b] = root_a
        elif self.heights[root_a] < self.heights[root_b]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.heights[root_a] += 1
        self.components -= 1

        return True


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        network = DisjointSet(n)

        for timestamp, x, y in sorted(logs, key=lambda log: log[0]):
            network.union(x, y)

            if network.components == 1:
                return timestamp

        return -1
