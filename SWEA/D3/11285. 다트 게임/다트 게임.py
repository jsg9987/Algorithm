# 5/7 22:00 ~
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    result = 0
    for _ in range(n):
        x, y = map(int, input().split())
        for p in range(10,0,-1):
            r = 20 * (11-p)
            dot_dist = x**2 + y**2
            if dot_dist <= r**2:
                result += p
                break

    print(f"#{tc} {result}")
