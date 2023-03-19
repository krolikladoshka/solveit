# https://codeforces.com/contest/1806/problem/A

for _ in range(int(input())):
    a, b, c, d = [int(x) for x in input().split()]
    if d == b:
        if a < c:
            print(-1)
        else:
            print(abs(c - a))
    elif b > d:
        print(-1)
    else:
        offset_diagonal = abs(d - b)
        count = offset_diagonal

        a += offset_diagonal
        b += offset_diagonal
        if d == b and a < c:
            print(-1)
        else:
            print(count + abs(c - a))
