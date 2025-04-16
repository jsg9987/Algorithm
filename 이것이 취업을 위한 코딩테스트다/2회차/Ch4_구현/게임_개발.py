# 4/15 21:05~15(구현)~
# 1. 현재 위치에서 현재 방향을 기준을오 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전 후 한칸 전진한다. 가보지 않은 칸이 없다면, 회전만 하고 1단계로 돌아간다
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있다면, 방향을 유지하고 한 칸 뒤로 가고 1단계로 돌아간다.(단, 뒤가 바다라면 stop)

n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
a, b, d = map(int, input().split())  # 좌표, direction

board = [list(map(int, input().split())) for _ in range(n)]
board[a][b] = 2
result = 1


def dfs(x, y):
    global result, d
    for i in range(4):
        if d-1 < 0:
            d = 3
        else:
            d = d - 1
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                result += 1
                return dfs(nx, ny)
    nx = x - dx[d]
    ny = y - dy[d]
    if board[nx][ny] != 1:
        return dfs(nx, ny)
    elif board[nx][ny] == 1:
        return True


while True:
    if dfs(a,b):
        break

print(result)