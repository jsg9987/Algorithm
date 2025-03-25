x = int(input())
min_count = [0] * 30001
min_count[1], min_count[2], min_count[3], min_count[5] = 0, 1, 1, 1

for i in range(2, len(min_count)):
    cnt = float('INF')
    if i % 5 == 0:
        if min_count[i // 5] + 1 < cnt:
            cnt = min_count[i // 5] + 1
            min_count[i] = cnt
    if i % 3 == 0:
        if min_count[i // 3] + 1 < cnt:
            cnt = min_count[i // 3] + 1
            min_count[i] = cnt
    if i % 2 == 0:
        if min_count[i // 2] + 1 < cnt:
            cnt = min_count[i // 2] + 1
            min_count[i] = cnt
    if min_count[i - 1] + 1 < cnt:
        cnt = min_count[i - 1] + 1
        min_count[i] = cnt

print(min_count[x])
