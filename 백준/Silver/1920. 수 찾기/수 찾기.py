# 5/14 20:00 ~
import sys

def binary_search(start, end, value):
    # 종료 조건: start > end
    if start > end:
        return

    mid = (start + end) // 2

    if li[mid] == value:
        return True
    elif value < li[mid]:
        return binary_search(start, mid-1, value)
    elif value > li[mid]:
        return binary_search(mid+1, end, value)


inputF = sys.stdin.readline
n = int(inputF())
li = list(map(int, inputF().split()))
li.sort()
m = int(inputF())
to_find = list(map(int, inputF().split()))

for i in to_find:
    if binary_search(0,n-1,i):
        print(1)
    else:
        print(0)
