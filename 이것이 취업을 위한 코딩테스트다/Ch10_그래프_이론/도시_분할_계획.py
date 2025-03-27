import sys
from collections import deque
inputF = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):  # 루트 부모가 같지 않을 때 사용 필요
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, inputF().split())
parent = [i for i in range(n+1)]

edges = []
result = 0

for _ in range(m):
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
max_cost = 0
# 필요 없는 간선 제거(최소 신장 트리 ->노드 -1개의 간선만 필요함)
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent, a, b)
        max_cost = max(max_cost, cost)
        result += cost

result -= max_cost
print(result)
