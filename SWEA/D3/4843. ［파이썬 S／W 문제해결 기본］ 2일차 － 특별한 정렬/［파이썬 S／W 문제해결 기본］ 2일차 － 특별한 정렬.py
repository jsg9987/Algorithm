from collections import deque

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    queue = deque(sorted(li))
    result = []
    right = True

    while len(result) != 10:
        if right:
            result.append(queue.pop())
            right = False
        else:
            result.append(queue.popleft())
            right = True

    print(f"#{tc} {' '.join(map(str, result))}")
