# 4/16 17:17~18:06
# 조건 1. 방문할 수 있는 정점이 여러 개인 경우 작은 번호부터
# 1 <= N <= 1000, 1 <= M <= 10000
# 아이디어: 간선이 양방향이므로 인접 행렬을 사용
import sys
from collections import deque
from copy import deepcopy

INF = int(1e9)
inputF = sys.stdin.readline
n, m, v = map(int, inputF().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
graph2 = deepcopy(graph)
for i in range(n + 1):
    graph[i][i], graph2[i][i] = 0, 0
for i in range(m): # "양방향" 처리를 까먹어서 시간 많이 뺏김
    start, arrive = map(int, inputF().split())
    graph[start][arrive], graph2[start][arrive] = 1, 1
    graph[arrive][start], graph2[arrive][start] = 1, 1
dfs_result = []
bfs_result = []
dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

def dfs(v):
    # 결과에 추가
    dfs_result.append(v)
    # 방문 처리 # 방문 처리를 거리를 INF로 바꿔서 처리하려다 시간을 많이 뺏김
    dfs_visited[v] = 1
    # 다음 노드 깊이 우선 탐색
    for i in range(n + 1):
        if graph[v][i] == 1 and not dfs_visited[i]:
            dfs(i)
    return


def bfs(v):
    queue = deque([v])

    while queue:
        x = queue.popleft()
        if bfs_visited[x]:
            continue
        # 결과 추가
        bfs_result.append(x)
        # 방문 처리
        bfs_visited[x] = 1
        for i in range(n + 1):
            if graph2[x][i] == 1:
                queue.append(i)
    return


dfs(v)
bfs(v)
print(*dfs_result)
print(*bfs_result)
