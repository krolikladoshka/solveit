n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    first, second = 1, 1
    sum = 2

    for i in range(2, n):
        first, second = second, first + second
        sum += second
    print(sum)
