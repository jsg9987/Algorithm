import copy
import sys
from itertools import combinations

def dfs(temp_board, x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx <= n - 1 and ny >= 0 and ny <= m - 1:
            if temp_board[nx][ny] == 0:  # 전 코드의 문제점: x,y좌표를 하나만 썼다. 처음에 함수에 들어갈때의 좌표는 2고 재귀호출되면 확인해야할 좌표는 0이어야함.
                # 따라서 nx,ny를 이용해서 재귀호출을 해야할 것 같음.
                temp_board[nx][ny] = 2
                dfs(temp_board, nx, ny)

        # 잘못 쓴 코드 -> 한 방향이라도 범위 밖이면 return을 하면서 함수를 빠져나가게 되버림. 따라서 정상작동하지 않음.
        # if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
        #     return
        # if temp_board[nx][ny] == 0: # 전 코드의 문제점: x,y좌표를 하나만 썼다. 처음에 함수에 들어갈때의 좌표는 2고 재귀호출되면 확인해야할 좌표는 0이어야함.
        #     # 따라서 nx,ny를 이용해서 재귀호출을 해야할 것 같음.
        #     temp_board[nx][ny] = 2
        #     dfs(temp_board, nx, ny)



inputF = sys.stdin.readline
n, m = map(int, inputF().split())
board = [list(map(int, inputF().split())) for _ in range(n)]
zero_coordinate = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            zero_coordinate.append((i, j))

candidates = list(combinations(zero_coordinate, 3))
safe_area = 0

for candidate in candidates:
    temp_board = copy.deepcopy(board)
    # 선택한 좌표에 벽 설치
    for x, y in candidate:
        temp_board[x][y] = 1
    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 2:
                dfs(temp_board, i, j)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 0:
                cnt += 1
    safe_area = max(safe_area, cnt)

print(safe_area)

# 처음 오류 코드
# import copy
# import sys
# from itertools import combinations
#
# sys.setrecursionlimit(100000)
# def dfs(temp_board, x, y):
#     if x < 0 or x > n - 1 or y < 0 or y > n - 1:
#         return False
#     # x,y 좌표를 변화 시켜준 다음에 해당 좌표가 0인지 확인하는 코드가 필요함
#     # nx, ny가 0이면 해당 좌표를 2로 바꿔주고 다시 dfs를 돌도록 해야함.
#     if temp_board[x][y] == 1:
#         return False
#     if temp_board[x][y] == 0:
#         temp_board[x][y] = 2
#         dfs(temp_board, x-1, y)
#         dfs(temp_board, x+1, y)
#         dfs(temp_board, x, y-1)
#         dfs(temp_board, x, y+1)
#
#     return False
#
#
#
#
# inputF = sys.stdin.readline
# n, m = map(int, inputF().split())
# board = [list(map(int, inputF().split())) for _ in range(n)]
# zero_coordinate = []
# for i in range(n):
#     for j in range(m):
#         if board[i][j] == 0:
#             zero_coordinate.append((i, j))
#
# candidates = list(combinations(zero_coordinate, 3))
# safe_area = 0
#
# for candidate in candidates:
#     temp_board = copy.deepcopy(board)
#     # 선택한 좌표에 벽 설치
#     for x, y in candidate:
#         temp_board[x][y] = 1
#     for i in range(n):
#         for j in range(m):
#             if temp_board[i][j] == 2:
#                 dfs(temp_board, i, j)
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if temp_board[i][j] == 0:
#                 cnt += 1
#     safe_area = max(safe_area, cnt)
#
# print(safe_area)