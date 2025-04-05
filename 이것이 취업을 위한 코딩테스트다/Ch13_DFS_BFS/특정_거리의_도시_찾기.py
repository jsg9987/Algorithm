from collections import deque
import sys
# 시간 복잡도: 노드 개수 N(300,000), 간선 개수 M(1,000,000) O(N+M)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                distance[i] = distance[v] + 1
                queue.append(i)
                visited[i] = True

input = sys.stdin.readline
INF = int(1e9)
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [INF] * (n + 1)
distance[x] = 0
visited = [False for _ in range(n+1)]
result = []
bfs(graph, x,visited)

for i, dist in enumerate(distance):
    if dist == k:
        result.append(i)

if not result:
    print(-1)
else:
    for i in result:
        print(i)
