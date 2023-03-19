# https://codeforces.com/contest/1807/problem/D

prefixes = [0] * (2 * (10 ** 5) + 1)

for _ in range(int(input())):
    n, q = map(int, input().split())
    array = map(int, input().split())

    for i, value in enumerate(array, start=1):
        prefixes[i] = prefixes[i - 1] + value

    for i in range(q):
        start, end, replace_value = map(int,    input().split())

        excluded_sum = prefixes[end] - prefixes[start - 1]
        replaced_sum = replace_value * (end - start + 1)

        if (prefixes[n] - excluded_sum + replaced_sum) & 1:
            print('yes')
        else:
            print('no')
