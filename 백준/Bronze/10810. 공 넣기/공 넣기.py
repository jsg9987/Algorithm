import sys

inputF = sys.stdin.readline
n,m = map(int, inputF().rstrip().split())
listA = [0 for i in range(n)]
for i in range(m):
    i,j,k = map(int, inputF().rstrip().split())

    for t in range(i-1,j):
        listA[t] = k

for i in listA:
    print(i, end=" ")