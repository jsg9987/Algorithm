board = [list(map(int, input().split())) for _ in range(9)]


def possible_num(row, col):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if board[i][col] in nums:
            nums.remove(board[i][col])

    for i in range(9):
        if board[row][i] in nums:
            nums.remove(board[row][i])

    nx = (row // 3) * 3
    ny = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[nx + i][ny + j] in nums:
                nums.remove(board[nx + i][ny + j])
    return nums


check = False


def dfs():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                possible = possible_num(i, j)
                if possible: # 가능한 숫자가 없다면 return
                    for num in possible:
                        board[i][j] = num
                        dfs()
                        board[i][j] = 0
                return

    for line in board:
        print(*line)
    exit()
dfs()
