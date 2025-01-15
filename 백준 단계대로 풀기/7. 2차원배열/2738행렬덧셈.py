# 입력
# 첫째 줄에 행렬 크기 N,M 주어짐
# 둘째 줄부터 N개의 줄에 원소 M개가 차례대로 주어짐.

# 출력
# 첫째 줄부터 N개의 줄에 행렬 A,B 더한 행렬 출력

import sys

inputF = sys.stdin.readline

# 1. 입력 및 변수 초기화
a = []
b = []
n,m = map(int, inputF().rstrip().split())
result = [[0 for _ in range(m)] for i in range(n)]

for i in range(n):
    vector = list(map(int, inputF().rstrip().split()))
    a.append(vector)

for i in range(n):
    vector = list(map(int, inputF().rstrip().split()))
    b.append(vector)

for i in range(n):
    for j in range(m):
        result[i][j] = a[i][j] + b[i][j]

for i in range(n):
    for j in range(m):
        print(result[i][j], end=" ")
    print()
