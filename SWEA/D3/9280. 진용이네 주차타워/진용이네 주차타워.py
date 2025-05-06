# 5/6 16:05 ~
# 주차장이 꽉 차면 대기해야한다.
from collections import deque
INF = int(1e9)

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    charges = list(int(input()) for _ in range(n))
    weights = list(int(input()) for _ in range(m))
    orders = list(int(input()) for _ in range(2 * m))
    queue = deque(orders)
    result = 0
    parking_lot = [0] * n
    idxes = [INF] * (m+1)
    waiting = deque([])

    while queue:
        x = queue.popleft()
        if x > 0:
            for i in range(n):
                if parking_lot[i] == 0:
                    result += weights[x-1] * charges[i]
                    parking_lot[i] = 1
                    idxes[x] = i
                    break
            else:
                waiting.append(x)
        elif x < 0:
            if idxes[-x] == INF:
                waiting.append(x)
                continue
            idx = idxes[-x]
            parking_lot[idx] = 0
            if waiting:
                next_car = waiting.popleft()
                result += weights[next_car-1] * charges[idx]
                parking_lot[idx] = 1
                idxes[next_car] = idx

    print(f"#{tc} {result}")

