T = int(input())

for tc in range(1, T+1):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0] * 8
    n = int(input())

    for i in range(len(money)):
        while n >= money[i]:
            n -= money[i]
            result[i] += 1

    print(f"#{tc}")
    print(*result)
