# 4/17 21:37~22:17
# BFS, visited 필요
# 틀린 점: 다음 층은 최대 층 수 f를 넘어갈 수 없다.
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0] * 1000001


def bfs(s):
    visited[s] = 1  # 방문 처리
    queue = deque([(s, 0)])

    while queue:
        v, cnt = queue.popleft()
        if v == g:
            return cnt
        for next_stair in (v + u, v - d):
            if 1 <= next_stair <= f:
                if not visited[next_stair]:
                    visited[next_stair] = 1
                    queue.append((next_stair, cnt + 1))
    return -1


result = bfs(s)
if result == -1:
    print("use the stairs")
else:
    print(result)
