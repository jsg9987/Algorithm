# 4/28 18:55 ~
# bfs로 최장 경로 계산
from collections import deque

T = int(input())

def dfs(start, length):
    global max_len
    max_len = max(max_len, length)

    for i in graph[start]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, length + 1)
            visited[i] = 0


for tc in range(1, T+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(m):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    max_len = 1
    for i in range(1, n+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    
    print(f"#{tc} {max_len}")