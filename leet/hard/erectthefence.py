from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(x, y, r) -> int:
            return (
                    (y[1] - x[1]) * (r[0] - y[0])
                    -
                    (y[0] - x[0]) * (r[1] - y[1])
            )

        def in_between(x, i, y) -> bool:
            x_in_between = (
                    (x[0] <= i[0] <= y[0])
                    or
                    (y[0] <= i[0] <= x[0])
            )
            y_in_between = (
                    (x[1] <= i[1] <= y[1])
                    or
                    (y[1] <= i[1] <= x[1])
            )

            return x_in_between and y_in_between

        def distance(x, y) -> int:
            return (y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2

        if len(trees) < 4:
            return trees

        leftmost = 0
        for i, p in enumerate(trees):
            if trees[i][0] < trees[leftmost][0]:
                leftmost = i

        convex_hull = set()
        current = leftmost
        while True:
            next_point = (current + 1) % len(trees)
            print(current, next_point)
            for i in range(len(trees)):
                if tuple(trees[i]) in convex_hull:
                    continue

                rightmost = orientation(trees[current], trees[i], trees[next_point])

                if rightmost < 0:
                    next_point = i
            print('#', current, next_point)
            for i in range(len(trees)):
                if i == current or i == next_point:
                    continue

                colinear = orientation(
                    trees[current],
                    trees[i],
                    trees[next_point]
                )
                if colinear != 0:
                    continue

                if in_between(trees[current], trees[i], trees[next_point]):
                    convex_hull.add(tuple(trees[i]))

            convex_hull.add(tuple(trees[next_point]))
            current = next_point

            if leftmost == current:
                return list(convex_hull)
