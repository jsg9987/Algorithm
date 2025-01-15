import sys

inputF = sys.stdin.readline

n,m = map(int, inputF().rstrip().split())
arr = list(range(1, n+1))
for k in range(m):
    i,j = map(int, inputF().rstrip().split())
    while j>i:    
        temp = arr[j-1]
        arr[j-1] = arr[i-1]
        arr[i-1] = temp
        i+=1
        j-=1

for i in arr:
    print(i, end=" ")