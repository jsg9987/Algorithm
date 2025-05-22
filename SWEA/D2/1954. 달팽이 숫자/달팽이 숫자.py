# 5/21 23:22 ~
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    x, y = 0, 0
    num = 1
    board[x][y] = num

    while num < n * n:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1 or board[nx][ny] != 0:
            dir = (dir + 1) % 4
        elif board[nx][ny] == 0:
            num += 1
            board[nx][ny] = num
            x = nx
            y = ny

    print(f"#{tc}")
    for row in board:
        print(*row)
