# https://codeforces.com/contest/1807/problem/A

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a + b == c:
        print('+')
    elif a - b == c:
        print('-')
