# https://codeforces.com/contest/1800/problem/C2
from heapq import heappush, heappop

cases = int(input())

for _ in range(cases):
    size = int(input())
    deck = []
    total_army_power = 0

    for card_power in map(int, input().split()):
        if card_power > 0:
            heappush(deck, -card_power)
        elif deck:
            total_army_power += -heappop(deck)
    print(total_army_power)
