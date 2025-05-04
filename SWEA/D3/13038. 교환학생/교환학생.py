# 5/4 16:30 ~
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    min_result = int(1e9)

    # 각 요일에 대해서 완전탐색하여 가장 적게 걸린 요일을 고르자
    for idx in range(7):
        temp_min = 0
        day_taken = 0
        while day_taken != n:
            temp_min += 1
            if li[idx] == 1:
                day_taken += 1
            idx = (idx + 1) % 7
        min_result = min(min_result, temp_min)

    print(f"#{tc} {min_result}")