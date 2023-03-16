# https://codeforces.com/contest/1800/problem/A
cases = int(input())

for _ in range(cases):
    sound_length = int(input())
    sound = input()

    meow = 'meow'
    transformed = []
    prev = ''
    for c in sound:
        c = c.lower()
        if c != prev:
            prev = c
            transformed.append(c)

    print('YES' if ''.join(transformed) == meow else 'NO')
