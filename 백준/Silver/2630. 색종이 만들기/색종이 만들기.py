# 5/13 17:40 ~ 18:40
import sys


def process(board):
    global white, blue
    length = len(board)

    # 종료 조건: 전부 한가지 색깔
    if one_color(board):
        if check_color(board) == 0:
            white += 1
        elif check_color(board) == 1:
            blue += 1
        return
    else:
        process([row[:length // 2] for row in board[:length // 2]])
        process([row[length // 2:] for row in board[:length // 2]])
        process([row[:length // 2] for row in board[length // 2:]])
        process([row[length // 2:] for row in board[length // 2:]])


def check_color(board):
    return board[0][0]


def one_color(board):
    length = len(board)
    flag = True
    # first = 0
    # if type(board) == int:
    #     first = board
    # elif type(board) == list:
    first = board[0][0]

    for i in range(length):
        for j in range(length):
            if board[i][j] != first:
                flag = False
                break
        if not flag:
            break

    return flag


inputF = sys.stdin.readline
n = int(inputF().rstrip())
board = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0
process(board)
print(white)
print(blue)
