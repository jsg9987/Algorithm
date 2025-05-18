# 5/18 16:56 ~
T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())
    result = ((a % 24) + b) % 24

    print(f"#{tc} {result}")
