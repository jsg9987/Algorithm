# union find(서로소 집합 알고리즘 문제 -> 경로 압축 기법 적용 시 O(V + MlogV)
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    # a = parent[a]
    # b = parent[b]
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for i in range(m):
    choice, a, b = map(int, input().split())
    if choice == 0:
        # 팀 합치기(부모가 달라야한다)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
    elif choice == 1:
        # 같은 팀 여부 확인
        # if parent[a] == parent[b]:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

