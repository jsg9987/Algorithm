from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간 밖으로 나갔을 때 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽일 때 무시
            if ice[nx][ny] == 0:
                continue
            # 다음 경로일 때
            if ice[nx][ny] == 1:
                ice[nx][ny] = ice[x][y] + 1
                queue.append((nx,ny))

    return ice[n-1][m-1]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
ice = [list(map(int, input())) for _ in range(n)]

print(bfs(0,0))