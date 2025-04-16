# 4/16 21:24~57
# BFS로 찾다가 출구를 찾으면 종료시킨다.
# 아이디어: 해당칸에 이동한 칸 수를 넣으면 마지막 칸의 이동 횟수를 알 수 있다.
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    queue = deque([(x,y)])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx,ny))


bfs(0,0)
print(board[n-1][m-1])