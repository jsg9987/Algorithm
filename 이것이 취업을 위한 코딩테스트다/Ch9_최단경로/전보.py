import heapq
import sys # 많은 개수의 입출력 필요
# 다익스트라 구현

# 무한값
INF = int(1e9)
input = sys.stdin.readline # 입출력 빠르게 하기위함.
n, m, c = map(int, input().split())

# 최단 거리 리스트
distance = [INF for _ in range(n + 1)]

# 도시에서 도시로 가는 정보 저장할 그래프 초기화
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0  # c -> c 거리 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)
least_time = [x for x in distance if 0 < x < INF]
city_cnt, latest_time = len(least_time), max(least_time)
print(city_cnt, latest_time)
