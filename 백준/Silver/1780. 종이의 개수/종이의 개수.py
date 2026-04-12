# 5/14 16:08 ~ 33
import sys


def process(x, y, length):
    global minus, zero, one

    # 검사했을 때 한 가지 숫자이면 global 키우고 종료
    if one_num(x, y, length):
        value = check_num(x, y, length)
        if value == -1:
            minus += 1
            return
        elif value == 0:
            zero += 1
            return
        elif value == 1:
            one += 1
            return

    # 검사했을 때 한 가지 숫자가 아니면 분할 재귀
    else:
        next_length = length // 3
        process(x, y, next_length)
        process(x, y + next_length, next_length)
        process(x, y + next_length * 2, next_length)
        process(x + next_length, y, next_length)
        process(x + next_length, y + next_length, next_length)
        process(x + next_length, y + next_length * 2, next_length)
        process(x + next_length * 2, y, next_length)
        process(x + next_length * 2, y + next_length, next_length)
        process(x + next_length * 2, y + next_length * 2, next_length)


def one_num(x, y, length):
    first = board[x][y]
    for i in range(length):
        for j in range(length):
            if board[x + i][y + j] != first:
                return False

    return True


def check_num(x, y, length):
    return board[x][y]


inputF = sys.stdin.readline
n = int(inputF().rstrip())
board = [list(map(int, inputF().rstrip().split())) for _ in range(n)]
minus, zero, one = 0, 0, 0
process(0, 0, n)

print(minus)
print(zero)
print(one)
