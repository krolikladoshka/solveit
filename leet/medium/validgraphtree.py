# https://leetcode.com/problems/graph-valid-tree
from collections import deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if n - 1 != len(edges):
        #     return False

        parents = [node for node in range(n)]
        sizes = [1] * n

        def find(node):
            root = node

            while root != parents[root]:
                root = parents[root]

            while node != root:
                old_root = parents[node]
                parents[node] = root
                node = old_root
            return node

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False
            if sizes[root_a] < sizes[root_b]:
                parents[root_a] = root_b
                sizes[root_b] += sizes[root_a]
            else:
                parents[root_b] = root_a
                sizes[root_a] += sizes[root_b]
            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return False
        return True

    def validTree_bfs(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        graph = [[] for _ in range(n)]

        for connection in edges:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])

        visited = {0}
        queue = deque([0])

        while queue:
            node = queue.popleft()

            for node in graph[node]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        return len(visited) == n
