from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 넣을 연결 리스트(graph) 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # A -> B
    # 진입차수 1 증가
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐 빌때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    print(*result)

topology_sort()
