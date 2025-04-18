# 4/18 20:45~

n, m = map(int, input().split())
r, c, d = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def turn_left():
    global d
    if d-1 < 0:
        d = 3
    else:
        d -= 1

def found_dirty(r,c):
    for dir in range(4):
        nr = r + dx[dir]
        nc = c + dy[dir]
        if 0 <= nr <= n - 1 and 0 <= nc <= m - 1:
            if board[nr][nc] == 0 and not visited[nr][nc]:
                return True
    return False

while True:
    if board[r][c] == 0:
        visited[r][c] = 1
        board[r][c] = 2

    if not found_dirty(r,c):
        nr = r - dx[d]
        nc = c - dy[d]
        if board[nr][nc] == 1:
            break
        else:
            r = nr
            c = nc
    elif found_dirty(r,c):
        turn_left()
        nr = r + dx[d]
        nc = c + dy[d]
        if board[nr][nc] == 0:
            r = nr
            c = nc

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            result += 1

print(result)