# 4/18 11:41
# 아이디어: 각 빙산 칸은 동시에 줄어들기 시작해야하므로 bfs
# 시간 초과
import copy
from collections import deque
import sys

inputF = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, inputF().split())
board = [[0] * m for _ in range(n)]
coordinates = []
for i in range(n):
    row = list(map(int, inputF().split()))
    for j in range(m):
        if row[j] == 0:
            coordinates.append((i, j))
        board[i][j] = row[j]


def check(board):
    temp_board = copy.deepcopy(board)
    result = 0
    for i in range(len(temp_board)):
        for j in range(len(temp_board[0])):
            if temp_board[i][j] > 0:
                bfs(i, j, temp_board)
                result += 1
    if result >= 2:
        return True


def bfs(i, j, temp_board):
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                if temp_board[nx][ny] > 0:
                    temp_board[nx][ny] = 0
                    queue.append((nx, ny))


def all_zero(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                return False
    return True


result = 0
while True:
    new_zero = []
    for x, y in coordinates:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                if board[nx][ny] > 0:
                    board[nx][ny] -= 1
                    if board[nx][ny] == 0:
                        new_zero.append((nx, ny))

    result += 1
    coordinates += new_zero
    if check(board):
        print(result)
        break
    if all_zero(board):
        print(0)
        break
