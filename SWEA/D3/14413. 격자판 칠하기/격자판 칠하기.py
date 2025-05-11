from collections import deque

T = int(input())

def possible(board):
    all_qm = True
    for i in range(n):
        for j in range(m):
            if board[i][j] != '?':
                all_qm = False
    if all_qm:
        return "possible"

    for x in range(n):
        for y in range(m):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= n -1 and 0 <= ny <= m-1:
                    if board[nx][ny] == board[x][y]:
                        return "impossible"

    return "possible"

for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    queue = deque([])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(n):
        for j in range(m):
            if board[i][j] == '#' or board[i][j] == '.':
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if board[nx][ny] == '?':
                    if board[x][y] == '.':
                        board[nx][ny] = '#'
                        queue.append((nx,ny))
                    if board[x][y] == '#':
                        board[nx][ny] = '.'
                        queue.append((nx,ny))

    result = possible(board)
    print(f"#{tc} {result}")
