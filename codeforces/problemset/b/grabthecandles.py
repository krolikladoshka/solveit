# https://codeforces.com/contest/1807/problem/B

for _ in range(int(input())):
    _ = input()
    candle_bags = map(int, input().split())

    even, odd = 0, 0
    for candles in candle_bags:
        if candles & 1:
            odd += candles
        else:
            even += candles
    print('yes' if even > odd else 'no')
