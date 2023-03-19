from typing import List, Iterable


class DisjointSetBase:
    def find(self, vertex):
        raise NotImplemented

    def union(self, a, b) -> bool:
        raise NotImplemented

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def find_roots(self, *vertecies) -> Iterable:
        return map(self.find, vertecies)


class QuickFindDisjointSet(DisjointSetBase):
    def __init__(self, n: int):
        self.size: int = n
        self.roots: List[int] = [i for i in range(n)]

    def find(self, vertex: int) -> int:
        return self.roots[vertex]

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        for vertex, root in enumerate(self.roots):
            if root == root_b:
                self.roots[vertex] = root_a

        return True


class QuickUnionDisjointSet(DisjointSetBase):
    def __init__(self, n: int):
        self.size: int = n
        self.parents: List[int] = [i for i in range(n)]

    def find(self, vertex: int) -> int:
        while vertex != self.parents[vertex]:
            vertex = self.parents[vertex]

        return vertex

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find_roots(a, b)

        if root_a == root_b:
            return False

        self.parents[root_b] = root_a

        return True


class RankedDisjointSet(DisjointSetBase):
    def __init__(self, n: int):
        self.size: int = n
        self.heights: List[int] = [1] * n
        self.parents: List[int] = [i for i in range(n)]

    def find(self, vertex: int) -> int:
        while vertex != self.parents[vertex]:
            vertex = self.parents[vertex]

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


class DisjointSet(DisjointSetBase):
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
