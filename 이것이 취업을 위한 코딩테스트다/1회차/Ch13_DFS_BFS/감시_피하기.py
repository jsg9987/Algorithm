from itertools import combinations

# 틀린 부분 1. dfs문을 return하지 않아서 결과가 상위로 전달되지 않았다.
# 2. 장애물 경우의 수를 board에 설치하고 원상복구하지 않은 심각한 오류가 있었다.
def dfs(x,y, in_progress, direction):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    if board[x][y] == 'S':
        return True
    if board[x][y] == 'O':
        return False

    if not in_progress:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if dfs(nx,ny, True, i):
                    return True
    elif in_progress:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
            if dfs(nx, ny, True, direction):
                return True
    return False


n = int(input())
board = [list(input().split()) for _ in range(n)]
coordinates = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'X':
            coordinates.append((i,j))

candidates = list(combinations(coordinates, 3))
check = False
for candidate in candidates:
    case_possible = True
    for x, y in candidate:
        board[x][y] = 'O'

    for x in range(n):
        for y in range(n):
            if board[x][y] == 'T':
                if dfs(x,y,False,None):
                    case_possible = False
    for x, y in candidate:
        board[x][y] = 'X'

    if case_possible:
        check = case_possible

if check:
    print("YES")
else:
    print("NO")