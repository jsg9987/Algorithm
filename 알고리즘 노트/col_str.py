

def col_str(board): # 열 추출
    return ''.join(str(board[row][0]) for row in range(0, len(board)))
