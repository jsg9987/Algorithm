if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    result = []
    min_count1 = 64
    min_count2 = 64
    for _ in range(n):
        board.append(list(input()))

    for i in range(0, n - 7):
        for j in range(0, m - 7):
            first = 'B'
            count = 0
            for row in range(i, i + 8):
                for col in range(j, j + 8):
                    if i % 2 == row % 2 and j % 2 == col % 2 and board[row][col] != first:
                        count += 1
                    if i % 2 != row % 2 and j % 2 == col % 2 and board[row][col] == first:
                        count += 1
                    if i % 2 == row % 2 and j % 2 != col % 2 and board[row][col] == first:
                        count += 1
                    if i % 2 != row % 2 and j % 2 != col % 2 and board[row][col] != first:
                        count += 1

            if count < min_count1:
                min_count1 = count
    result.append(min_count1)
                
    for i in range(0, n - 7):
        for j in range(0, m - 7):
            first = 'W'
            count = 0
            for row in range(i, i + 8):
                for col in range(j, j + 8):
                    if i % 2 == row % 2 and j % 2 == col % 2 and board[row][col] != first:
                        count += 1
                    if i % 2 != row % 2 and j % 2 == col % 2 and board[row][col] == first:
                        count += 1
                    if i % 2 == row % 2 and j % 2 != col % 2 and board[row][col] == first:
                        count += 1
                    if i % 2 != row % 2 and j % 2 != col % 2 and board[row][col] != first:
                        count += 1

            if count < min_count2:
                min_count2 = count
    result.append(min_count2)

    print(min(result))
