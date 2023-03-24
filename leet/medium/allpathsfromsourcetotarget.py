# https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph_size = len(graph)
        paths = []

        adjaceny_list = [[] for i in range(graph_size)]
        for i in range(graph_size):
            for neighbour in graph[i]:
                adjaceny_list[i].append(neighbour)

        def backtrack(node, path):
            if node == graph_size - 1:
                # path.append(node)
                paths.append(path[:])

                return

            for neighbour in graph[node]:
                path.append(neighbour)
                backtrack(neighbour, path)
                path.pop()

        backtrack(0, [0])

        return paths
