n = int(input())
board = [[" " for _ in range(n)] for _ in range(n)]


def star(start_i, start_j, n):
    # n이 3인 경우
    if n == 3:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    board[start_i+i][start_j+j] = "*"
    # n이 3보다 큰 경우
    else:
        for i in range(0, (n // 3) * 2 + 1, n // 3):
            for j in range(0, (n // 3) * 2 + 1, n // 3):
                if i != n // 3 or j != n // 3:
                    star(start_i + i, start_j + j, n // 3)

star(0,0,n)
for line in board:
    print(*line, sep="")