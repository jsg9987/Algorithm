INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 경로 거리 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 정보 입력 받아, 값 초기화
for _ in range(m):
    #a -> b
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 #양방향

x, k = map(int, input().split())

# 점화식에 맞게 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # 양방향이니까 가는길,오는길 모두 1

if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])