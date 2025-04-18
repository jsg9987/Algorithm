# 4/18 11:41
# 아이디어: 각 빙산 칸은 동시에 줄어들기 시작해야하므로 bfs
# 구현 순서에서 전체 흐름을 써두자.
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                if not visited[nx][ny] and board[nx][ny] > 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


def count_ice_parts():
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1
    return cnt


def melt():
    temp = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if board[x][y] > 0:
                water = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and board[nx][ny] == 0:
                        water += 1
                temp[x][y] = max(0, board[x][y] - water)
    return temp


year = 0
while True:
    parts = count_ice_parts()
    if parts == 0:
        print(0)
        break
    if parts >= 2:
        print(year)
        break
    board = melt()
    year += 1
