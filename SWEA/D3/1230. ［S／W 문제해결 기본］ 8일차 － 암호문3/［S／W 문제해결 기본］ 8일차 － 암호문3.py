from collections import deque

cmd_chr = ['I', 'D', 'A']


for tc in range(1, 11):
    n = int(input())
    origin = list(map(int, input().split()))
    cmd_cnt = int(input())
    queue = deque(input().split())

    while queue:
        chr = queue.popleft()
        if chr in cmd_chr:
            if chr == 'I':
                idx = int(queue.popleft())
                cnt = int(queue.popleft())
                codes = [int(queue.popleft()) for _ in range(cnt)]
                origin = origin[:idx] + codes + origin[idx:]
            elif chr == 'D':
                idx = int(queue.popleft())
                cnt = int(queue.popleft())
                del origin[idx-1:idx-1+cnt]
            elif chr == 'A':
                cnt = int(queue.popleft())
                codes = [int(queue.popleft()) for _ in range(cnt)]
                origin += codes

    print(f"#{tc}", end=" ")
    print(*origin[:10])