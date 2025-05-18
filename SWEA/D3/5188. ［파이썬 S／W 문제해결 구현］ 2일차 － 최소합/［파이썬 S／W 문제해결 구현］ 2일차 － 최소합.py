from collections import deque

T = int(input())


def bfs(i, j, num_sum):
    global min_result
    dx = [0, 1]
    dy = [1, 0]
    queue = deque([(i, j, num_sum)])

    while queue:
        x, y, total = queue.popleft()
        if x == n - 1 and y == n - 1:
            min_result = min(min_result, total)
            continue

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] < total + board[nx][ny]:
                    continue
                visited[nx][ny] = total + board[nx][ny]
                queue.append((nx, ny, total + board[nx][ny]))


for tc in range(1, T + 1):
    n = int(input())
    INF = int(1e9)
    board = [list(map(int, input().split())) for _ in range(n)]
    min_result = INF
    visited = [[INF] * n for _ in range(n)]
    bfs(0, 0, board[0][0])

    print(f"#{tc} {min_result}")
