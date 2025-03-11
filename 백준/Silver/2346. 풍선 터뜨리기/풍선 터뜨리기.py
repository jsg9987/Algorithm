import sys
from collections import deque

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    q = deque(enumerate(map(int, inputF().rstrip().split())))
    li = []
    while q:
        idx, num = q.popleft()
        li.append(idx + 1)

        if num > 0:
            q.rotate(-(num - 1))
        elif num < 0:
            q.rotate(-num)

    for i in li:
        print(i, end=" ")
