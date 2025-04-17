# 4/17 16:02~17:20 시간 초과
# 문제점: 익은 토마토에서 너비 우선 탐색을 하는 bfs를 구현했지만 실제론 한 점마다 실행했기에 깊이 우선 탐색처럼 작동하였다.
# 모든 익은 토마토에서 너비 우선 탐색을 하도록 익은 토마토 좌표를 모두 큐에 넣고 bfs를 실행해야 한다.
# 아이디어: BFS를 사용하여 전이되어 익은 토마토 칸에 해당 날짜를 넣는다.
from collections import deque

m, n, h = map(int, input().split())
box = [[] for _ in range(n)]
for i in range(h):
    for _ in range(n):
        box[i].append(list(map(int, input().split())))

visited = [[[0] * m for _ in range(n)] for _ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]  # 위,아래,왼,오,앞,뒤
dy = [0, 0, 0, 0, 1, -1]
dz = [0, 0, -1, 1, 0, 0]

def reset_visited():
    return [[[0] * m for _ in range(n)] for _ in range(h)]

def bfs(x, y, z):
    visited[x][y][z] = 1  # 방문 처리
    queue = deque([(x,y,z)])

    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx <= h-1 and 0 <= ny <= n-1 and 0 <= nz <= m-1:
                if not visited[nx][ny][nz]:
                    visited[nx][ny][nz] = 1
                    if box[nx][ny][nz] == 0:
                        box[nx][ny][nz] = box[x][y][z] + 1
                        queue.append((nx,ny,nz))
                    elif box[nx][ny][nz] > 0:
                        box[nx][ny][nz] = min(box[nx][ny][nz], box[x][y][z] + 1)
                        queue.append((nx,ny,nz))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                bfs(i, j, k)
                visited = reset_visited()

max_day = 0
result = 0
flag = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                result = -1
                flag = True
                break
            if box[i][j][k] > 0:
                result = max(result, box[i][j][k] - 1)
        if flag:
            break
    if flag:
        break

print(result)