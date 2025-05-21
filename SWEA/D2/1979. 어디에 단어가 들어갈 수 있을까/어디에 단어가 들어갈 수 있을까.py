T = int(input())


def check_right(x, y):
    if y + k - 1 >= n:
        return False

    for i in range(k):
        if board[x][y + i] != 1:
            return False

    if y + k == n:
        return True

    if y + k < n:
        if board[x][y + k] == 0:
            return True


def check_down(x, y):
    if x + k - 1 >= n:
        return False

    for i in range(k):
        if board[x + i][y] != 1:
            return False

    if x + k == n:
        return True

    if x + k < n:
        if board[x + k][y] == 0:
            return True


for tc in range(1, T + 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    possible_coordinates = []
    result = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i == 0:  # 위가 막힌 경우
                    if check_down(i, j):
                        result += 1

                elif board[i - 1][j] == 0:
                    if check_down(i, j):
                        result += 1

                if j == 0:  # 왼쪽 막힌 경우
                    if check_right(i, j):
                        result += 1
                elif board[i][j - 1] == 0:
                    if check_right(i, j):
                        result += 1

    print(f"#{tc} {result}")
