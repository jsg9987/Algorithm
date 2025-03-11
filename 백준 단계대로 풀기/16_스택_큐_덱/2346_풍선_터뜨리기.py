import sys
from collections import deque

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    q = deque(enumerate(map(int, inputF().rstrip().split())))
    result = []

    while q:
        idx, move = q.popleft()
        result.append(idx + 1)

        if q:
            if move > 0:
                for _ in range(move - 1):
                    q.append(q.popleft())
            elif move < 0:
                for _ in range(-move):
                    q.appendleft(q.pop())

    for idx in result:
        print(idx, end=" ")

