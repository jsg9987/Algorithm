# 4/17 20:49~21:12
# 걷는다면 1초 후 X-1, X+1로 이동, 순간이동하면 1초 후 2*X로 이동
# "가장 빠른 시간" -> BFS가 좋아보임.
# 아이디어: 위치,초를 넣어서 BFS로 탐색하다 K와 같으면 초를 return하자
from collections import deque

n, k = map(int, input().split())
visited = [0] * (1000001)


def bfs(n):
    queue = deque([(n, 0)])

    while queue:
        x, time = queue.popleft()
        visited[x] = 1
        nx = 0
        if x == k:
            return time
        # for i in range(3):
        #     if i == 0:
        #         nx = x - 1
        #     elif i == 1:
        #         nx = x + 1
        #     elif i == 2:
        #         nx = 2 * x
        #     if 0 <= nx <= 100000 and not visited[nx]:
        #         visited[nx] = 1
        #         queue.append((nx, time+1))
        # 코드 개선
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = 1
                queue.append((nx, time+1))
print(bfs(n))

