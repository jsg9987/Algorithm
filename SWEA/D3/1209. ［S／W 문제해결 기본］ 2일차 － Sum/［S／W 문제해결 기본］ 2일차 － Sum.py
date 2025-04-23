# 4/23 17:05 ~ 16

for _ in range(1, 11):
    tc = int(input())

    li = [list(map(int, input().split())) for _ in range(100)]
    max_result = 0
    # 가로
    for i in range(100):
        temp_sum = sum(li[i])
        if temp_sum > max_result:
            max_result = temp_sum

    # 세로
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            temp_sum += li[j][i]
        if temp_sum > max_result:
            max_result = temp_sum

    # 대각선
    temp = 0
    temp2 = 0
    for i in range(100):
        temp += li[i][i]
        temp2 += li[i][99-i]
    max_result = max(max_result, temp, temp2)
    print(f"#{tc} {max_result}")
