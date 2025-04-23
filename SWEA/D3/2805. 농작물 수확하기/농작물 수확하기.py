# 4/23 17:29 ~ 17:58

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    mid = n // 2
    i = 0
    row = 0
    result = 0
    while mid - i >= 0:
        for j in range(mid - i, mid + i + 1):
            result += board[row][j]
        i += 1
        row += 1
    i = mid-1

    while i >= 0:
        for j in range(mid - i, mid + i + 1):
            result += board[row][j]
        i -= 1
        row += 1
    print(f"#{tc} {result}")