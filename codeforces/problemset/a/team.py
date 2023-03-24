# https://codeforces.com/problemset/problem/231/A
from functools import reduce

n = int(input())

implemented_problems = 0

for _ in range(n):
    voting = reduce(lambda x, y: x + y, map(int, input().split()), 0)

    if voting >= 2:
        implemented_problems += 1

print(implemented_problems)
