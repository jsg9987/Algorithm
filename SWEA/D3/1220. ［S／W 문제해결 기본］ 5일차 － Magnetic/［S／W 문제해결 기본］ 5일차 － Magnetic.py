# 4/24 17:14 ~ 42
# bfs
# 교착 판단은 상하로 1,2가 있는 경우에만
from collections import deque


def check(board):
    result = 0
    for i in range(len(board[0])):
        for j in range(len(board) - 1):
            above = board[j][i]
            under = board[j + 1][i]
            if above == 1 and under == 2:
                result += 1
    return result


def bfs(queue):
    while queue:
        x, y, pole = queue.popleft()
        nx, ny = 0, y
        if pole == 1:
            nx = x + 1
        elif pole == 2:
            nx = x - 1
        if 0 <= nx <= len(board) - 1 and 0 <= ny <= len(board[0]) - 1:
            if board[nx][ny] == 0:
                board[x][y] = 0
                board[nx][ny] = pole
                queue.append((nx, ny, pole))


for tc in range(1, 11):
    n = int(input())
    board = []
    coordinates = []
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if row[j] == 1:
                coordinates.append((i, j, 1))
            elif row[j] == 2:
                coordinates.append((i, j, 2))
        board.append(row)

    queue = deque(coordinates)
    bfs(queue)
    print(f"#{tc} {check(board)}")
