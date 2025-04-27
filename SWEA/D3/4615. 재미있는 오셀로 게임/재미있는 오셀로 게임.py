# 4/27 17:57 ~ 18:44

T = int(input())

dr = [-1, 1, 0, 0, -1, -1, 1, 1]  # 상하좌우, 대각선
dc = [0, 0, -1, 1, -1, 1, -1, 1]


def process(row, col, stone):
    for dir in range(8):
        flag = False
        nr = row
        nc = col
        while True:
            nr += dr[dir]
            nc += dc[dir]
            if nr < 0 or nr > n - 1 or nc < 0 or nc > n - 1:
                break
            if board[nr][nc] == 0:
                break
            if board[nr][nc] == stone:
                while True:
                    if nr == row and nc == col:
                        flag = True
                        break
                    nr -= dr[dir]
                    nc -= dc[dir]
                    board[nr][nc] = stone
            if flag:
                break


for tc in range(1, T + 1):
    n, m = map(int, input().split())  # 보드 길이
    board = [[0] * n for _ in range(n)]
    mid = n // 2
    board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1
    board[mid][mid] = 2
    for _ in range(m):
        col, row, stone = map(int, input().split())
        row -= 1
        col -= 1
        board[row][col] = stone
        process(row, col, stone)

    black, white = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f"#{tc} {black} {white}")
