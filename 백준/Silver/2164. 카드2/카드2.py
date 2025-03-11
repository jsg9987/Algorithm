import sys
from collections import deque

if __name__ == '__main__':
    n = int(input())

    queue = deque([i for i in range(1, n + 1)])
    while len(queue) != 1:
        queue.popleft()
        v = queue.popleft()
        queue.append(v)

    print(queue[0])