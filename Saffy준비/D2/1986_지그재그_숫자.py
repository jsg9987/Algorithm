T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    result = 0

    for i in range(1, n+1):
        if i % 2 == 0:
            result -= i
        else:
            result += i

    print(f"#{test_case} {result}")
