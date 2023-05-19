# https://leetcode.com/problems/sum-of-distances-in-tree/
from typing import List, Optional


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [list() for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        counts: List[int] = [1 for _ in range(n)]
        sums: List[int] = [0 for _ in range(n)]

        def dfs(node: int, parent: Optional[int] = None):
            for child in graph[node]:
                if child == parent:
                    continue

                dfs(child, node)
                counts[node] += counts[child]
                sums[node] += sums[child] + counts[child]
        dfs(0)

        def dfs_neighbours(node: int, parent: Optional[int] = None):
            for child in graph[node]:
                if child == parent:
                    continue
                child_count = counts[child]
                sums[child] = sums[node] - child_count + n - child_count

                dfs_neighbours(child, node)

        print(sums)
        dfs_neighbours(0)
        print(sums)
        return counts
