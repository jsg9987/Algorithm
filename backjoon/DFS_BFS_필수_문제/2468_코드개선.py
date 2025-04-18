import copy
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0
visited = [[0] * n for _ in range(n)]

def set_board(board, height):
    temp_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(n):
            if temp_board[i][j] <= height:
                temp_board[i][j] = 0
    return temp_board


def reset_visited():
    return [[0] * n for _ in range(n)]


def bfs(x,y):
    global temp_board
    visited[x][y] = 1
    temp_board[x][y] = 0
    queue = deque([(x,y)])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if not visited[nx][ny] and temp_board[nx][ny] > 0:
                    temp_board[nx][ny] = 0
                    visited[nx][ny] = 1
                    queue.append((nx,ny))


for i in range(0,101):
    temp_board = set_board(board, i)
    visited = reset_visited()
    temp_result = 0
    for x in range(n):
        for y in range(n):
            if temp_board[x][y] > 0:
                bfs(x,y)
                temp_result += 1
    result = max(result, temp_result)

print(result)
