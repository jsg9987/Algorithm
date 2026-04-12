import sys

inputF = sys.stdin.readline

n,m = map(int,inputF().rstrip().split())

arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = i+1

for k in range(m):
    i,j = map(int, inputF().rstrip().split())
    temp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = temp

for i in arr:
    print(i, end=" ")