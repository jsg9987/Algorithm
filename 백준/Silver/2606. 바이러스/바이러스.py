# 4/16 22:01~
# 아이디어: 인접 리스트를 이용해서 새로운 노드를 방문할 때마다 컴퓨터 수를 늘려준다.
# 조건: 1 <= N <= 100, m , 양방향
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n+1) # 방문 확인
for _ in range(m):
    start, arrive = map(int, input().split())
    graph[start].append(arrive)
    graph[arrive].append(start)

result = 0
def bfs(v):
    global result
    queue = deque([v])
    visited[v] = 1

    while queue:
        x = queue.popleft()
        # 방문 처리
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                result += 1

bfs(1)
print(result)