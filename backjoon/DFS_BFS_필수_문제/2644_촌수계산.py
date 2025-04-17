# 4/17 14:43~15:23
# DFS로 촌수를 전달해서 찾으려는 번호를 찾을때까지 촌수를 키워가며 찾는다. 찾으면 촌수를 return
# 조건: 양방향 graph, 촌수 계산이 불가능하면 -1 출력(-1 return)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n+1)
for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)


def dfs(x, y, cnt):
    visited[x] = 1
    if y in graph[x]:
        return cnt

    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            result = dfs(i,y, cnt+1)
            if result != -1:
                return result
            # return dfs(i,y,cnt+1) 오류: 결과가 있을 수도 있는데 먼저 -1을 찾으면 결과를 찾기 전에 -1을 return해버림
    return -1

print(dfs(a, b, 1))
