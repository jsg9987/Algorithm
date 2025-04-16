# 4/16 22:44
#
from collections import deque

n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
house_cnt = []


def bfs(x, y, cnt):
    house_cnt = 1
    board[x][y] += cnt
    visited[x][y] = 1
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    board[nx][ny] += cnt
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    house_cnt += 1
    return house_cnt


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house_cnt.append(bfs(i, j, cnt))
            cnt += 1

house_cnt.sort()
print(cnt-1)
for i in house_cnt:
    print(i)
