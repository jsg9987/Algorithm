# 5/9 14:52 ~
T = int(input())

for tc in range(1, T + 1):
    d, h, m = map(int, input().split())
    start_m, start_h, start_d = 11,11,11
    if d == 11 and h == 11 and m < 11 or d == 11 and h < 11 or d < 11:
        print(f"#{tc} -1")
        continue
    minute, hour, day = 0, 0, 0
    if m < start_m:
        start_h += 1
        minute = 60 - start_m + m
    else:
        minute = m - start_m

    if h < start_h:
        start_d += 1
        hour = 24 - start_h + h
    else:
        hour = h - start_h
    day = d - start_d

    result = day * 24 * 60 + hour * 60 + minute
    print(f"#{tc} {result}")

