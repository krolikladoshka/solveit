# https://leetcode.com/problems/find-if-path-exists-in-graph
from collections import deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = [[] for i in range(n)]

        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        queue = deque([source])
        visited = {source}

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for neighbour in adjacency_list[node]:
                if neighbour not in visited:
                    visited.add(neighbour)

                    queue.append(neighbour)
        return False
