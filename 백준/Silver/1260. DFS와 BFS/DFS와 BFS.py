# 4/16 18:20~ 38
import sys
from collections import deque

INF = int(1e9)
inputF = sys.stdin.readline
n, m, v = map(int, inputF().split())
# 인접 리스트를 이용
dfs_graph = [[] for _ in range(n+1)]
bfs_graph = [[] for _ in range(n+1)]
for i in range(m): # 양방향 처리 필요
    start, arrive = map(int, inputF().split())
    dfs_graph[start].append(arrive)
    bfs_graph[start].append(arrive)
    dfs_graph[arrive].append(start)
    bfs_graph[arrive].append(start)
dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

def dfs(v):
    # 결과 출력
    print(v, end=" ")
    # 방문 처리
    dfs_visited[v] = 1
    # 깊이 우선 탐색으로 처리
    # for i in range(n+1): # 마찬가지로 불필요하게 모든 노드를 확인 중
    #     if i in dfs_graph[v] and not dfs_visited[i]: 
    for i in sorted(dfs_graph[v]):
        if not dfs_visited[i]:
            dfs(i)
    return


def bfs(v):
    queue = deque([v])

    while queue:
        x = queue.popleft()
        if not bfs_visited[x]:
            # 결과 출력
            print(x, end=" ")
        # 방문 처리
        bfs_visited[x] = 1
        # for i in range(n+1): # 100만, 해당 노드에서 출발해서 도착하는 경우만 보면되는데, 불필요하게 확인하고 있음.
        #     if i in bfs_graph[x] and not bfs_visited[i]:
        for i in sorted(bfs_graph[x]):
            if not bfs_visited[i]:
                queue.append(i)
    return

dfs(v)
print()
bfs(v)
