T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    pre_li = [1]
    next_li = []
    print(f"#{test_case}")
    print(*pre_li)

    for i in range(n):
        if i == 0:
            continue
        next_li = [0 for _ in range(i+1)]

        for j in range(i+1):
            if j == 0 or j == len(next_li) -1:
                next_li[j] = 1
            else:
                next_li[j] = pre_li[j-1] + pre_li[j]

        print(*next_li)
        pre_li = next_li

