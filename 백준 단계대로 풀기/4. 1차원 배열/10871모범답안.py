import sys
inputF = sys.stdin.readline

n,x = map(int, inputF().rstrip().split())
listA = list(map(int, inputF().rstrip().split()))
for i in range(n):
    if listA[i] < x:
        print(listA[i], end=" ")


