T = int(input())

for tc in range(1, T+1):
    d, h, m = map(int, input().split())
    start = 11 * 24 * 60  + 11 * 60 + 11
    end = d * 24 * 60 + h * 60 + m
    result = end - start
    if result < 0:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {result}")