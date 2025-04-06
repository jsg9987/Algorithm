import sys
from collections import deque


# 오답 -> 초를 처리하기 위해서 불필요하게 그 전 좌표를 큐에 다시 넣었음.
# 초를 처리하는 방법: 전파되는 좌표를 넣을 때 튜플에 시간 + 1을 저장하면 된다.
def bfs(board, queue, k, s):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    time = 1

    while queue:
        virus, time, x, y = queue.popleft()
        if time == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 좌표가 시험관을 벗어나지 않거나 다음 좌표에 이미 바이러스가 존재하지 않을 때
            if 0 <= nx <= len(board) - 1 and 0 <= ny <= len(board) - 1 and board[nx][ny] == 0:
                board[nx][ny] = virus
                queue.append((virus, time + 1, nx, ny))

        prev = virus


inputF = sys.stdin.readline
n, k = map(int, inputF().split())
board = [list(map(int, inputF().split())) for _ in range(n)]
s, x, y = map(int, inputF().split())
li = []

for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            li.append((board[i][j], 0, i, j))

li.sort(key=lambda x: x[0])
queue = deque(li)
bfs(board, queue, k, s)

print(board[x - 1][y - 1])
