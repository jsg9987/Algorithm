# 4/25 15:37 ~ 16:00
from collections import deque

for tc in range(1, 11):
    n = int(input())
    origin = list(map(int, input().split()))
    order_cnt = int(input())
    orders = input().split()
    queue = deque(orders)

    while queue:
        if queue.popleft() == 'I':
            idx = int(queue.popleft())
            cnt = int(queue.popleft())
            nums = []
            for _ in range(cnt):
                num = int(queue.popleft())
                nums.append(num)
            origin = origin[:idx] + nums + origin[idx:]

    print(f"#{tc} {' '.join(str(i) for i in origin[:10])}")