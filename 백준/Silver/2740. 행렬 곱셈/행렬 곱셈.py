# 5/14 20:09 ~ 21:11
import sys

inputF = sys.stdin.readline
n,m = map(int, inputF().split())
a = [list(map(int, inputF().split())) for _ in range(n)]
m,k = map(int, inputF().split())
b = [list(map(int, inputF().split())) for _ in range(m)]
matrix = [[0] * k for _ in range(n)]

for i in range(n):
    a_row = a[i]
    for j in range(k):
        temp = 0
        for l in range(m):
            temp += a_row[l] * b[l][j]
        matrix[i][j] = temp

for row in matrix:
    print(*row)

