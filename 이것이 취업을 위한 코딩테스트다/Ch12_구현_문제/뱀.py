import sys
from collections import deque

inputF = sys.stdin.readline
n = int(inputF())
board = [[0 for _ in range(n)] for _ in range(n)]
k = int(inputF())
for _ in range(k):
    row, col = map(int, inputF().rstrip().split())
    board[row - 1][col - 1] = 2
dic = dict()
l = int(inputF())
for _ in range(l):
    x, c = inputF().rstrip().split()
    dic[int(x)] = c
board[0][0] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0
x = 0
y = 0
body_coordinate = deque([(0,0)])

for i in range(1, 10001):
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 벽이나 자신의 몸과 부딪히면 end
    if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board) or board[nx][ny] == 1:
        print(i)
        break
    # 다음 칸에 사과가 있으면 꼬리는 이동 x
    if board[nx][ny] == 0:
        tail_x, tail_y = body_coordinate.popleft()
        board[tail_x][tail_y] = 0
    # 다음 칸에 사과가 없으면 꼬리가 위치한 칸을 비워준다.
    # else: # 문제점: 몸통이 길때는 바로 뒷칸이 꼬리가 아니다! 꼬리의 위치를 별도 저장해줘야한다.
    #     board[x][y] = 0
    x = nx
    y = ny
    board[x][y] = 1
    body_coordinate.append((x,y))
    if i in dic:
        if dic[i] == 'L':
            if dir - 1 < 0:
                dir = 3
            else:
                dir -= 1
        elif dic[i] == 'D':
            dir = (dir + 1) % 4



