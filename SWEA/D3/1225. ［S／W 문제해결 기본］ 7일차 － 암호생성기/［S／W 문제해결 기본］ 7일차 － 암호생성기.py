# 4/24 15:29
from collections import deque

T = 10

for _ in range(1, T+1):
    tc = int(input())
    li = list(map(int, input().split()))
    queue = deque(li)
    check = True
    while check:
        for i in range(1,6):
            v = queue.popleft() - i
            if v <= 0:
                v = 0
                queue.append(v)
                check = False
                break
            else:
                queue.append(v)
    result = list(map(str, queue))
    print(f"#{tc} {' '.join(result)}")