# https://codeforces.com/problemset/problem/1794/C
from collections import deque

cases = int(input())

for _ in range(cases):
    length = int(input())
    values = map(int, input().split())
    queue = deque()

    for value in values:
        queue.append(value)

        while queue and queue[0] < len(queue):
            queue.popleft()
        print(len(queue), end=' ')
    print()
