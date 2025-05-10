T = int(input())

for _ in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for i in reversed(range(n)):
        if board[0][i] != 0 * n + i + 1:
            cnt += 1
            for j in range(i+1):
                for k in range(j+1):
                    board[j][k], board[k][j] = board[k][j], board[j][k]

    print(cnt)
