# 4/30 21:48 ~

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    stop_cnt = [0] * 5001
    result = []
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            stop_cnt[i] += 1

    p = int(input())
    for _ in range(p):
        c = int(input())
        result.append(stop_cnt[c])

    print(f"#{tc} {' '.join(str(i) for i in result)}")