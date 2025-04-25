# 4/25 16:13 ~ 17:01
# 포탄을 발사 시 맵 밖으로 나갈 때 까지 직진, 포탄이 벽(*)에 부딪힐 시 평지(.)로 바뀐다.


T = int(input())


def move_possible(x, y):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx <= h - 1 and 0 <= ny <= w - 1:
        if board[nx][ny] != '-' and board[nx][ny] != '#' and board[nx][ny] != '*':
            return True
    return False


def shoot(x, y):
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx > h-1 or ny < 0 or ny > w-1:
            break
        if board[nx][ny] == '#':
            break
        if board[nx][ny] == '*':
            board[nx][ny] = '.'
            break
        x = nx
        y = ny

for tc in range(1, T + 1):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    n = int(input())
    order = input()
    x, y = 0, 0
    dir = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(h):
        for j in range(w):
            if board[i][j] == '^' or board[i][j] == 'v' or board[i][j] == '<' or board[i][j] == '>':
                x = i
                y = j
            if board[i][j] == '^':
                dir = 0
                break
            if board[i][j] == 'v':
                dir = 1
                break
            if board[i][j] == '<':
                dir = 2
                break
            if board[i][j] == '>':
                dir = 3
                break

    for i in range(len(order)):
        now_order = order[i]
        if now_order == 'U':
            dir = 0
            if move_possible(x, y):
                board[x][y] = '.'
                x = x + dx[dir]
                y = y + dy[dir]
            board[x][y] = '^'
        if now_order == 'D':
            dir = 1
            if move_possible(x, y):
                board[x][y] = '.'
                x = x + dx[dir]
                y = y + dy[dir]
            board[x][y] = 'v'
        if now_order == 'L':
            dir = 2
            if move_possible(x, y):
                board[x][y] = '.'
                x = x + dx[dir]
                y = y + dy[dir]
            board[x][y] = '<'
        if now_order == 'R':
            dir = 3
            if move_possible(x, y):
                board[x][y] = '.'
                x = x + dx[dir]
                y = y + dy[dir]
            board[x][y] = '>'
        if now_order == 'S':
            shoot(x, y)

    print(f"#{tc}", end=" ")
    for i in range(h):
        print(*board[i], sep='')