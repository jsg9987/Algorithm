from collections import deque


def bfs(x, y):
    queue = deque([[(x, y)]])
    global cnt
    maze[x][y] = cnt

    # n,m에 도착할 때까지 찾기
    while queue:
        v = queue.popleft()
        for i in v:
            if i[0] == n - 1 and i[1] == m - 1:
                print(cnt)
                break
        cnt += 1

        for i in v:
            nx, ny = i[0], i[1]
            li = []
            if nx + 1 < n and maze[nx + 1][ny] == 1: # 공간을 벗어날 때와 처음 방문했을 때의 경우를 분리 필요
                maze[nx + 1][ny] = cnt
                li.append((nx + 1, ny))
            if ny + 1 < m and maze[nx][ny + 1] == 1:
                maze[nx][ny + 1] = cnt
                li.append((nx, ny + 1))
            if nx - 1 >= 0 and maze[nx - 1][ny] == 1:
                maze[nx - 1][ny] = cnt
                li.append((nx - 1, ny))
            if ny - 1 >= 0 and maze[nx][ny - 1] == 1:
                maze[nx][ny - 1] = cnt
                li.append((nx, ny - 1)) # 문제점: append 코드가 반복되고 있다. range(4)로 모두 append하는 방식으로 개선 필요
            if li:
                queue.append(li)


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
cnt = 1

bfs(0, 0)
