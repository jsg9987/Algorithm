n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n+1)
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

def dfs(v, cnt): # 굳이 y까지 필요 x, 정점 하나만 넘기고 해당 정점이 y가 되면 return하면 됨.
    visited[v] = 1
    for i in graph[v]:
        if i == b:
            return cnt
        if not visited[i]:
            result = dfs(i, cnt+1)
            if result != -1:
                return result
    return -1

print(dfs(a,1))
