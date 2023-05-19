# https://leetcode.com/problems/jump-game-iv
from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        if len(arr) == 2:
            return 1

        graph = defaultdict(list)

        for i, val in enumerate(arr):
            if val in graph:
                graph[val].append(i)
            else:
                graph[val] = [i]

        seen = {0}
        queue = deque([(0, 0)])
        target = len(arr) - 1

        while queue:
            node, steps = queue.popleft()

            if node == target:
                return steps
            for child in graph[arr[node]]:

                if child not in seen:
                    seen.add(child)
                    queue.append((child, steps + 1))

            graph[arr[node]].clear()

            for child in filter(lambda x: 0 <= x < len(arr), [node - 1, node + 1]):
                if child not in seen:
                    seen.add(child)
                    queue.append((child, steps + 1))
        return -1
