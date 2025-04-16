# 4/16 16:31~
from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]


def bfs(x, y):
    queue = deque([])
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    board[x][y] = "2"
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if board[nx][ny] =="0":
                    board[nx][ny] = "2"
                    queue.append((nx,ny))
    return

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "0":
            bfs(i, j)
            result += 1

print(result)