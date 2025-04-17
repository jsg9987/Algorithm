# 4/17 22:25~
# dfs 사용
# 틀린점: 비가 오지 않을 수도 있다.-> 아무 지역도 물에 잠기지 않을 수 있다.
import copy
from sys import setrecursionlimit

setrecursionlimit(10**6)

def set_board(board, height):
    temp_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(n):
            if temp_board[i][j] <= height:
                temp_board[i][j] = 0

    return temp_board


def dfs(x, y):
    global temp_board
    temp_board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
            if not visited[nx][ny] and temp_board[nx][ny] > 0:
                visited[nx][ny] = 1
                dfs(nx, ny)


def reset_visited():
    return [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0
visited = [[0] * n for _ in range(n)]

for i in range(0, 101):
    temp_board = set_board(board, i)
    visited = reset_visited()
    temp_result = 0
    for x in range(n):
        for y in range(n):
            if temp_board[x][y] > 0:
                dfs(x, y)
                temp_result += 1
    result = max(result, temp_result)

print(result)