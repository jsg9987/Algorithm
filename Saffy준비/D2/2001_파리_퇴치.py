T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    li = []
    max_cnt = 0
    total = 0
    for _ in range(n):
        li.append(list(map(int, input().split())))

    for i in range(n-(m-1)):
        for j in range(n-(m-1)):
            total = 0
            for k in range(m):
                for l in range(m):
                    total += li[i + k][j + l]

            if total > max_cnt:
                max_cnt = total

    print(f"#{test_case} {max_cnt}")
