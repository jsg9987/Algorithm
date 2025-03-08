import sys
from collections import deque

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    A = list(map(int, inputF().rstrip().split()))
    B = deque(list(map(int, inputF().rstrip().split())))
    m = int(inputF().rstrip())
    C = list(map(int, inputF().rstrip().split()))

    queue = deque([])
    result = []

    for i in range(n):
        if A[i] == 0:
            queue.append(B[i])

    for i in C:
        if queue:
            result.append(queue.pop())
            queue.appendleft(i)
        else:
            result.append(i)

    print(' '.join(str(i) for i in result))

