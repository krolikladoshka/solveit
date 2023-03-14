cases = int(input())

for _ in range(cases):
    seen = set()
    length = int(input())
    tasks = input()
    sum = 0

    for i in range(length):
        if tasks[i] not in seen:
            seen.add(tasks[i])
            sum += 2
        else:
            sum += 1
    print(sum)
