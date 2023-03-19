# https://codeforces.com/contest/1807/problem/E


def solution():
    prefixes = [0] * (2 * (10 ** 5) + 1)

    def guess(start, end):
        print(f'? {end - start + 1} {" ".join(map(str, range(start, end + 1)))}', flush=True)

    def range_sum(start, end):
        return prefixes[end] - prefixes[start]

    for _ in range(int(input())):
        n = int(input())
        pile_nums = map(int, input().split())

        for i, value in enumerate(pile_nums, start=1):
            prefixes[i] = prefixes[i - 1] + value

        start = 1
        end = n
        found = -1

        while start <= end:
            mid = (start + end) // 2
            guess(start, mid)

            actual_sum = int(input())
            supposed_sum = range_sum(start - 1, mid)

            if actual_sum > supposed_sum:
                found = mid
                end = mid - 1
            else:
                start = mid + 1
        print(f'! {found}', flush=True)


solution()
