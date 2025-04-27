# 4/27 21:52 ~
from collections import deque

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split()) # N명의 사람, M초마다 K개의 붕어빵 생산
    times = list(map(int, input().split()))
    times.sort()
    queue = deque(times)
    store = 0
    idx = 0
    result = "Possible"

    for i in range(11112):
        if i % m == 0 and i != 0:
            store += k

        if queue:
            while queue[0] == i:
                v = queue.popleft()
                store -= 1
                if store < 0:
                    result = "Impossible"
                    break
                if not queue:
                    break

        if result == "Impossible":
            break
    print(f"#{tc} {result}")