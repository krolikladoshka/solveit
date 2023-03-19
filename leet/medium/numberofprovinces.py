# https://leetcode.com/problems/number-of-provinces/
from typing import List, Iterable


class DisjointSetCP:
    def __init__(self, n: int):
        self.size: int = n
        self.heights: List[int] = [1] * n
        self.parents: List[int] = [i for i in range(n)]

    def find(self, vertex: int) -> int:
        root = vertex

        while root != self.parents[root]:
            root = self.parents[root]

        while root != vertex:
            old_root = self.parents[vertex]
            self.parents[vertex] = root
            vertex = old_root

        return vertex

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find_roots(a, b)

        if root_a == root_b:
            return False

        if self.heights[root_a] > self.heights[root_b]:
            self.parents[root_b] = root_a
        elif self.heights[root_a] < self.heights[root_b]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.heights[root_a] += 1

        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def find_roots(self, *vertecies) -> Iterable:
        return map(self.find, vertecies)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities_graph = DisjointSetCP(len(isConnected))
        provinces = len(isConnected)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    if i != j and cities_graph.union(j, i):
                        provinces -= 1

        return provinces
