if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    result = []

    for _ in range(n):
        board.append(list(input()))

    for i in range(n - 7):
        for j in range(m - 7):
            draw1 = 0
            draw2 = 0
            for row in range(i, i + 8):
                for col in range(j, j + 8):
                    if (row + col) % 2 == 0:
                        if board[row][col] != 'B':
                            draw1 += 1
                        if board[row][col] != 'W':
                            draw2 += 1
                    else:
                        if board[row][col] != 'W':
                            draw1 += 1
                        if board[row][col] != 'B':
                            draw2 += 1
            result.append(draw1)
            result.append(draw2)
    print(min(result))