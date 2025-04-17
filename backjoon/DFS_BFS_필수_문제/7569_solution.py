# 핵심 아이디어: 다중 시작점 bfs
# 익은 토마토의 좌표를 모두 큐에 넣어 전이시킨다.
# 토마토가 처음부터 모두 익었는지는 입력할 때 확인하는게 편해보임.
# 문제와 예시를 직접 써가며 이해했다면 익은 토마토 좌표를 queue에 추가해야한다는 것을 파악했을 것이다. 문제, 예시 직접 그려보기
from collections import deque

m, n, h = map(int, input().split())
box = [[[0] * m for _ in range(n)] for _ in range(h)]
queue = deque()
all_ripe = True

for i in range(h):  # 리스트를 받고 좌표를 이용해서 입력하는 방식
    for j in range(n):
        row = list(map(int, input().split()))
        for k in range(m):  # 익은 토마토 큐에 저장
            box[i][j][k] = row[k]
            if row[k] == 0:
                all_ripe = False
            if row[k] == 1:
                queue.append((i, j, k))

if all_ripe:
    print(0)
    exit()

# 6방향
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(queue):
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx <= h - 1 and 0 <= ny <= n - 1 and 0 <= nz <= m - 1:
                if box[nx][ny][nz] == 0:
                    box[nx][ny][nz] = box[x][y][z] + 1
                    queue.append((nx, ny, nz))


bfs(queue)
result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, box[i][j][k])

print(result - 1)
