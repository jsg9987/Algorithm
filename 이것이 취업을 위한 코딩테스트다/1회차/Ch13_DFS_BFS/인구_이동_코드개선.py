import sys

sys.setrecursionlimit(10**6)
inputF = sys.stdin.readline
n, l, r = map(int, inputF().split())
board = [list(map(int, inputF().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
result = 0

def dfs(x,y, visited, union):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    visited[x][y] = 1
    union.append((x,y)) # union의 길이가 1 이상이면 국경선을 열었음.

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= n-1 and not visited[nx][ny]:
            diff = abs(board[nx][ny]- board[x][y])
            if l <= diff <= r:
                dfs(nx,ny, visited, union)

def move_people(union):
    total_population = sum(board[x][y] for x,y in union)
    new_population = total_population // len(union)
    for x,y in union:
        board[x][y] = new_population

moved = False
while True:

    # 국경선 open 검사
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = []
                dfs(i,j, visited, union)
                if len(union) >= 2:
                    moved = True
                    move_people(union)

    # 방문 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

    # 더 이상 인구 이동할 수 없다면 end
    if not moved:
        break
    result += 1

print(result)

























