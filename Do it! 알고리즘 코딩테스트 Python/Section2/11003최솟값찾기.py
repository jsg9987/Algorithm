import sys

inputF = sys.stdin.readline

n,l = map(int, inputF().rstrip().split())

arr = list(map(int, inputF().rstrip().split()))
arr2 = []
for i in range(n):
    if i-l<0:
        min = arr[0]
    else:
        min = arr[i-l+1]
    for j in range(i-l+1,i+1):
        if j<0:
            None
        else:
            if min>arr[j]:
                min = arr[j]
    arr2.append(min)

print(arr2, end=" ")