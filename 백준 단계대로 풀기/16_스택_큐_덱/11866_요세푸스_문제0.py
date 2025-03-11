import sys
from collections import deque

if __name__ == '__main__':
    n, k = map(int, input().split())
    queue = deque([i for i in range(1, n + 1)])
    li = []
    while len(queue) != 0:
        for _ in range(k-1):
            queue.append(queue.popleft())
        li.append(str(queue.popleft()))

    print('<' + ', '.join(li) + '>')