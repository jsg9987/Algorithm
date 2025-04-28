# 4/25 16:13 ~ 17:01
# 포탄을 발사 시 맵 밖으로 나갈 때 까지 직진, 포탄이 벽(*)에 부딪힐 시 평지(.)로 바뀐다.


T = int(input())


def move_possible(nx, ny):
    return 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.'


def shoot(x, y, dx, dy):
    nx, ny = x, y
    while True:
        nx += dx
        ny += dy
        if nx < 0 or nx > h - 1 or ny < 0 or ny > w - 1:
            break
        if board[nx][ny] == '#':
            break
        if board[nx][ny] == '*':
            board[nx][ny] = '.'
            break


dir_info = {'U': (0, '^', -1, 0), 'D': (1, 'v', 1, 0), 'L': (2, '<', 0, -1), 'R': (3, '>', 0, 1)}
tank_symbol = ['^', 'v', '<', '>']

for tc in range(1, T + 1):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    n = int(input())
    commands = input()
    x, y = 0, 0
    dir = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] in tank_symbol:
                x = i
                y = j
                dir = tank_symbol.index(board[i][j])
                break
        else:
            continue
        break

    for cmd in commands: # cmd를 기준으로 dx, dy, symbol, dir 등이 한번에 처리된다.
        if cmd in dir_info:
            dir, symbol, dx, dy = dir_info[cmd]
            board[x][y] = symbol
            nx, ny = x + dx, y + dy
            if move_possible(nx, ny):
                board[x][y] = '.'
                board[nx][ny] = symbol
        elif cmd == 'S':
            dx, dy = dir_info[tank_symbol[dir]][2], dir_info[tank_symbol[dir]][3]
            shoot(x,y,dx,dy)

    print(f"#{tc}", end=" ")
    for row in board:
        print(''.join(row))
