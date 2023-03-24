# https://codeforces.com/problemset/problem/158/B

n = int(input())
children_groups = map(int, input().split())

taxis = 0
full_cab = 0
counts = [0] * 5
for children_group in children_groups:
    counts[children_group] += 1

taxis = counts[2] // 2 + counts[3] + counts[4]

counts[1] -= counts[3]

if counts[2] & 1:
    taxis += 1
    counts[1] -= 2

if counts[1] > 0:
    taxis += (counts[1] + 3) // 4

print(taxis)
