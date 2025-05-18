# 5/18 18:26 ~
from collections import deque

for tc in range(1, 11):
    n = int(input())
    li = list(map(int, input().split()))
    cmd_cnt = int(input())
    cmds = deque(list(input().split()))

    while cmds:
        order = cmds.popleft()

        if order == 'I':
            idx = int(cmds.popleft())
            cnt = int(cmds.popleft())
            temp = []
            for _ in range(cnt):
                temp.append(int(cmds.popleft()))

            li = li[:idx] + temp + li[idx:]
        elif order == 'D':
            idx = int(cmds.popleft())
            cnt = int(cmds.popleft())
            for _ in range(cnt):
                del li[idx]

    print(f"#{tc} {' '.join(map(str, li[:10]))}")
