# 5/20 22:26 ~ 44

from collections import deque

T = int(input())

def bfs(start_x, start_y):
    global min_result

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(start_x, start_y, 0)])

    while queue:
        x, y, total = queue.popleft()

        # 좌표가 도착지일 경우 비교 후 continue
        if x == end[0] and y == end[1]:
            min_result = min(min_result, total)
            continue

        # 다음 좌표에 갈 수 있고, 더 짧은 시간이 걸린다면 갱신
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if total + board[nx][ny] < visited[nx][ny]:
                    visited[nx][ny] = total + board[nx][ny]
                    queue.append((nx, ny, total + board[nx][ny]))


for tc in range(1, T + 1):
    INF = int(1e9)
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    start = (0, 0)
    end = (n - 1, n - 1)
    min_result = INF
    visited = [[INF] * n for _ in range(n)]
    bfs(start[0], start[1])

    print(f"#{tc} {visited[n-1][n-1]}")
