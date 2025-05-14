# 5/14 22:34 ~
import sys

def binary_search(start, end):
    global max_len
    if start > end:
        return

    length = (start + end) // 2

    if check(length):
        max_len = max(max_len, length)
        binary_search(length+1, end)
    else:
        binary_search(start, length-1)


def check(length):
    cnt = 0

    for lan in cables:
        cnt += lan // length

    if cnt >= n:
        return True
    else:
        return False




inputF = sys.stdin.readline
k, n = map(int, inputF().split())
cables = [int(inputF().rstrip()) for _ in range(k)]
max_len = 0
binary_search(1,max(cables))
print(max_len)
