if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    result = []
    draw1 = 64
    draw2 = 64
    for _ in range(n):
        board.append(list(input()))

    for i in range(0, n - 7):
        for j in range(0, m - 7):
            first_B = 'B'
            first_W = 'W'
            count1 = 0
            count2 = 0
            for row in range(i, i + 8):
                for col in range(j, j + 8):
                    if i % 2 == row % 2 and j % 2 == col % 2 and board[row][col] != first_B:
                        count1 += 1
                    if i % 2 != row % 2 and j % 2 == col % 2 and board[row][col] == first_B:
                        count1 += 1
                    if i % 2 == row % 2 and j % 2 != col % 2 and board[row][col] == first_B:
                        count1 += 1
                    if i % 2 != row % 2 and j % 2 != col % 2 and board[row][col] != first_B:
                        count1 += 1

                    if i % 2 == row % 2 and j % 2 == col % 2 and board[row][col] != first_W:
                        count2 += 1
                    if i % 2 != row % 2 and j % 2 == col % 2 and board[row][col] == first_W:
                        count2 += 1
                    if i % 2 == row % 2 and j % 2 != col % 2 and board[row][col] == first_W:
                        count2 += 1
                    if i % 2 != row % 2 and j % 2 != col % 2 and board[row][col] != first_W:
                        count2 += 1
            if count1 < draw1:
                draw1 = count1
            if count2 < draw2:
                draw2 = count2
    result.append(draw1)
    result.append(draw2)

    print(min(result))
