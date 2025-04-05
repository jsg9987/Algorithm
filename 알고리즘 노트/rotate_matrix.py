def rotate_a_matrix_by_90_degree(board):
    n = len(board)
    m = len(board[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = board[i][j]
    return result
